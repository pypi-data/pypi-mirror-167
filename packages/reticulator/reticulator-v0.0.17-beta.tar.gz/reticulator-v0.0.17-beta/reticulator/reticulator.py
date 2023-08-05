from __future__ import annotations

import re
import os
import json
import glob
import functools 

from pathlib import Path
from functools import cached_property
from typing import Union, Tuple

import dpath.util

NO_ARGUMENT = object()
TEXTURE_EXTENSIONS = ["png", "jpg", "jpeg", "tga"]
SOUND_EXTENSIONS = ["wav", "fsb", "ogg"]

def convert_to_notify_structure(data: Union[dict, list], parent: Resource) -> Union[NotifyDict, NotifyList]:
    """
    Converts a dict or list to a notify structure.
    """
    if isinstance(data, dict):
        return NotifyDict(data, owner=parent)

    if isinstance(data, list):
        return NotifyList(data, owner=parent)

    return data

    #  setattr(cls, 'test', test_template)


def format_version(jsonpath: str = "format_version"):
    """
    Class Decorator which inserts a 'format_version property, with proper
    semantics.
    """

    def inner_format_version(cls):
        @property
        def format_version(self) -> FormatVersion:
            return FormatVersion(self.get_jsonpath(jsonpath))
        
        @format_version.setter
        def format_version(self, format_version):
            return self.set_jsonpath(jsonpath, str(FormatVersion(format_version)))

        cls.format_version = format_version
        return cls
    
    return inner_format_version


def identifier(jsonpath: str):
    """
    Class Decorator, which injects handling for accessing 'identifier'.
    :param jsonpath: The jsonpath where the identifier can be located.
    """

    def inner(cls):
        @property
        def identifier(self) -> str:
            return self.get_jsonpath(jsonpath)
        
        @identifier.setter
        def identifier(self, identifier):
            return self.set_jsonpath(jsonpath, identifier)

        cls.identifier = identifier
        
        return cls

    return inner

def class_property(attribute: str, jsonpath: str):
    """
    Class Decorator which injects a single 'property' with proper semantics.

    :param attribute: The attribute where this property can be accessed from
    :param jsonpath: The jsonpath where this attribute can be found in the json data
    """

    def inner(cls):
        @property
        def template_property(self) -> str:
            return self.get_jsonpath(jsonpath)
        
        @template_property.setter
        def template_property(self, identifier):
            return self.set_jsonpath(jsonpath, identifier)

        setattr(cls, attribute, template_property)

        return cls
    return inner

def sub_resource(*, cls: JsonSubResource, jsonpath : str):
    """
    Base decorator for doing a subresource type
    :param cls: The class you want to create, when parsing the data
    """

    # TODO: Store this on cls, and then make it private by injecting __
    attribute = '__render_controllers'

    def decorator(func):
        @cached_property
        @functools.wraps(func)
        def wrapper(self):
            setattr(self, attribute, [])
            for path, data in self.get_data_at(jsonpath):
                getattr(self, attribute).append(cls(parent = self, json_path = path, data = data))
            return getattr(self, attribute)
        return wrapper
    return decorator

def get_sub_resource(attribute: str, child_attribute: str):
    """
    Decorator which injects function information for 'getting' a subresource
    based on identifier
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, id):
            for child in getattr(self, attribute):
                if smart_compare(getattr(child, child_attribute), id):
                    return child
            raise AssetNotFoundError(id)
        return wrapper
    return decorator


def add_sub_resource(cls, jsonpath: str, attribute: str):
    """
    This decorator allows you to inject SubResources into your Resources.

    @param cls: The class to create, as a child.
    @param jsonpath: The jsonpath, representing where to inject the newly created resource.
    @param attribute: The attribute where this attribute will
    """
    def decorator_sub_resource(func):
        @functools.wraps(func)
        def wrapper_sub_resource(self, *args):
            if len(args) == 2 and isinstance(args[0], str):
                name = args[0]
                data = args[1]

                self.set_jsonpath(jsonpath + name, data)
                object = cls(data=data, parent=self, json_path=jsonpath + name)
                return object

            elif len(args) == 1 and isinstance(args[0], cls):
                object = args[0]

                self.set_jsonpath(object.json_path, object.data)
                object.parent = self
                getattr(self, attribute).append(object)
                return object
            else:
                # TODO: Fix this error message
                raise TypeError('Accepts either name and data or instance of class.')
        return wrapper_sub_resource
    return decorator_sub_resource

# Methods
def create_nested_directory(path: str):
    """
    Creates a nested directory structure if it doesn't exist.
    """
    Path(path).parent.mkdir(parents=True, exist_ok=True)

def save_json(file_path, data):
    """
    Saves json to a file_path, creating nested directory if required.
    """
    create_nested_directory(file_path)
    with open(file_path, "w+") as file_head:
        return json.dump(data, file_head, indent=2, ensure_ascii=False)

def smart_compare(a, b) -> bool:
    """
    Compares to objects using ==, but if they can both be interpreted as
    path-like objects, it uses path comparison.
    """
    try:
        a = Path(a)
        b = Path(b)

        return a == b
    except Exception:
        return a == b


# Exceptions
class ReticulatorException(Exception):
    """
    Base class for Reticulator exceptions.
    """

class FloatingAssetError(ReticulatorException):
    """
    Called when a "floating" asset attempts to access its parent pack, for
    example when saving
    """

class AssetNotFoundError(ReticulatorException):
    """
    Called when attempting to access an asset that does not exist, for
    example getting an entity by name
    """

class InvalidJsonError(ReticulatorException):
    """
    Called when a JSON file is invalid.
    """

class AmbiguousAssetError(ReticulatorException):
    """
    Called when a path is not unique.
    """

class FormatVersionError(ReticulatorException):
    """
    Called when a format version does not exist for a file
    """


# Base Classes

class NotifyDict(dict):
    """
    A notify dictionary is a dictionary that can notify its parent when its been
    edited.
    """
    def __init__(self, *args, owner: Resource = None, **kwargs):
        self._owner = owner

        if len(args) > 0:
            for key, value in args[0].items():
                args[0][key] = convert_to_notify_structure(value, self._owner)
        super().__init__(*args, **kwargs)

    def get_item(self, attr):
        try:
            return self.__getitem__(attr)
        except Exception:
            return None
    
    def __delitem__(self, v) -> None:
        if(self._owner != None):
            self._owner.dirty = True
        return super().__delitem__(v)

    def __setitem__(self, attr, value):
        value = convert_to_notify_structure(value, self._owner)

        if self.get_item(attr) != value:
            if(self._owner != None):
                self._owner.dirty = True

        super().__setitem__(attr, value)

class NotifyList(list):
    """
    A notify list is a list which can notify its owner when it has
    changed.
    """
    def __init__(self, *args, owner: Resource = None, **kwargs):
        self._owner = owner

        if len(args) > 0:
            for i in range(len(args[0])):
                args[0][i] = convert_to_notify_structure(args[0][i], self._owner)

        super().__init__(*args, **kwargs)

    def get_item(self, attr):
        try:
            return self.__getitem__(attr)
        except Exception:
            return None
    
    def __delitem__(self, v) -> None:
        if(self._owner != None):
            self._owner.dirty = True
        return super().__delitem__(v)
    
    def append(self, v):
        if(self._owner != None):
            self._owner.dirty = True
        super().append(v)

    def extend(self, v):
        if(self._owner != None):
            self._owner.dirty = True
        super().extend(v)

    def __setitem__(self, attr, value):
        value = convert_to_notify_structure(value, self._owner)

        if self.__getitem__(attr) != value:
            if(self._owner != None):
                self._owner.dirty = True
        
        super().__setitem__(attr, value)

class Pack():
    """
    Pack is a parent class that contains the shared functionality between the
    resource pack and the behavior pack.
    """
    def __init__(self, input_directory: str, project : Project = None):
        self.resources = []
        self._language_files = []
        self._project = project

        # The input path is the path to the folder containing the pack.
        self.input_path: str = input_directory

        # The output path is the path to the output directory, where this
        # pack will be saved. This is the same as the input path, unless
        # explicitely saved.
        self.output_directory: str = input_directory

    @cached_property
    def project(self) -> Project:
        """
        Get the project that this pack is part of. May be None.
        """
        return self._project

    def save(self, force=False):
        """
        Saves every child resource.
        """
        for resource in self.resources:
            resource.save(force=force)

    def register_resource(self, resource: Resource) -> None:
        """
        Register a child resource to this pack. These resources will be saved
        during save.
        """

        # Attempt to set the pack for this resource.
        try:
            resource.pack = self
        except Exception:
            pass
        self.resources.append(resource)

    def get_language_file(self, file_path:str) -> LanguageFile:
        """
        Gets a specific language file, based on the name of the language file.
        For example, 'texts/en_GB.lang'
        """
        for language_file in self.language_files:
            if smart_compare(language_file.file_path, file_path):
                return language_file
        raise AssetNotFoundError(file_path)

    @cached_property
    def language_files(self) -> list[LanguageFile]:
        """
        Returns a list of LanguageFiles, as read from 'texts/*'
        """
        base_directory = os.path.join(self.input_path, "texts")
        for local_path in glob.glob(base_directory + "/**/*.lang", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self._language_files.append(LanguageFile(file_path = local_path, pack = self))
            
        return self._language_files

class Project():
    """
    Project is a class which represents an entire 'addon', via references to a 
    ResourcePack and BehaviorPack, along with some helper methods.
    """
    def __init__(self, behavior_path: str, resource_path: str):
        self.__behavior_path = behavior_path
        self.__resource_path = resource_path
        self.__resource_pack : ResourcePack = None
        self.__behavior_pack : BehaviorPack = None
    
    def set_output_directory(self, save_location: str) -> None:
        """
        Sets the save location of the RP and the BP, based on the folder
        name from their input path.

        In other words, pass in a folder where you want both the RP and the BP 
        to be saved.

        If you need finer control, use the 'set_save_location' method on the 
        ResourcePack and BehaviorPack instead.
        """
        self.resource_pack.output_directory = save_location + "/" + os.path.dirname(self.resource_pack.input_path)
        self.behavior_pack.output_directory = save_location + "/" + os.path.dirname(self.behavior_pack.input_path)

    def get_packs(self) -> Tuple[behavior_pack, resource_pack]:
        """
        Returns Behavior Pack followed by ResourcePack.
        Useful for quickly defining rp and bp:
        rp, bp = Project("...").get_packs()
        """
        return self.behavior_pack, self.resource_pack
        
    @cached_property
    def resource_pack(self) -> ResourcePack:
        """
        The resource pack of the project.
        """
        self.__resource_pack = ResourcePack(self.__resource_path, project=self)
        return self.__resource_pack

    @cached_property
    def behavior_pack(self) -> BehaviorPack:
        """
        The behavior pack of the project.
        """
        self.__behavior_pack = BehaviorPack(self.__behavior_path, project=self)
        return self.__behavior_pack

    def save(self, force=False):
        """
        Saves both packs.
        """
        self.__behavior_pack.save(force=force)
        self.__resource_pack.save(force=force)


class Resource():
    """
    The top resource in the inheritance chain.

    Contains:
     - reference to the Pack (could be blank, if floating resource)
     - reference to the File (could be a few links up the chain)
     - dirty status
     - abstract ability to save, including context manager support
     - list of children resources
    """

    def __init__(self, file: FileResource = None, pack: Pack = None) -> None:
        # Public
        self.pack: Union[ResourcePack, BehaviorPack] = pack
        self.file = file
        self._dirty = False
        self._deleted = False

        # Private
        self._resources: Resource = []

    def __enter__(self) -> Resource:
        """
        Context manager support.
        """
        return self

    def __exit__(self, type, value, traceback):
        """
        Context manager support. Will save the resource on exit.
        """
        self.save()

    @property
    def dirty(self):
        """
        Whether the asset is dirty (has been edited).
        """
        return self._dirty

    @dirty.setter
    def dirty(self, dirty):
        self._dirty = dirty

    def register_resource(self, resource) -> None:
        """
        Register a child resource. These resources will always be saved first.
        """
        self._resources.append(resource)

    def _save(self):
        """
        Internal implementation of asset saving.

        Should always be implemented.
        """
        raise NotImplementedError()

    def _delete(self):
        """
        Internal implementation of asset deletion.

        Should always be implemented.
        """
        raise NotImplementedError()


    def save(self, force=False):
        """
        Saves the resource. Should not be overridden.

        This method will save all child resources first, by calling
        the internal _save implementation.
        """

        # File Assets without packs may not save.
        if isinstance(self, FileResource) and not self.pack:
            raise FloatingAssetError("Assets without a pack cannot be saved.")

        # Only dirty assets can be saved, unless forced.
        if self.dirty or force:
            # Save all children first
            for resource in self._resources:
                resource.save(force=force)

            # Now, save this resource
            self._save()

            # Mark as clean
            self.dirty = False


    def delete(self):
        """
        Deletes the resource. Should not be overridden.
        """

        # First, delete all resources of children
        for resource in self._resources:
            resource.delete()

        # Then delete self
        self._delete()

class FileResource(Resource):
    """
    A resource, which is also a file.
    Contains:
     - File path
     - Ability to mark for deletion
    """
    def __init__(self, file_path: str = None, pack: Pack = None) -> None:
        # Initialize resource
        super().__init__(file=self, pack=pack)

        # All files must register themselves with their pack
        # if the pack exists.
        if self.pack:
            pack.register_resource(self)

        # Public
        self.file_path = file_path

        if file_path:
            self.file_name = os.path.basename(file_path)

    def _delete(self):
        """
        Internal implementation of file deletion.

        Marking for deletion allows us to delete the file during saving,
        without effecting the file system during normal operation.
        """
        self._deleted = True

class JsonResource(Resource):
    """
    Parent class, which is responsible for all resources which contain
    json data.
    Should not be used directly. Use JsonFileResource, or JsonSubResource instead.
    Contains:
     - Data object
     - Method for interacting with the data
    """

    def __init__(self, data: dict = None, file: FileResource = None, pack: Pack = None) -> None:
        super().__init__(file=file, pack=pack)
        self._data = data
    
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self.dirty = True
        self._data = data

    def _save(self):
        raise NotImplementedError("This json resource cannot be saved.")

    def _delete(self):
        raise NotImplementedError("This json resource cannot be deleted.")

    def __str__(self):
        return json.dumps(self.data, indent=2, ensure_ascii=False)

    def jsonpath_exists(self, json_path:str) -> bool:
        """
        Checks if a jsonpath exists
        """
        try:
            self.get_jsonpath(json_path)
            return True
        except AssetNotFoundError:
            return False

    def delete_jsonpath(self, json_path:str) -> None:
        """
        Removes value at jsonpath location.
        """
        path_exists = self.jsonpath_exists(json_path)
        if path_exists:
            self.dirty = True
            dpath.util.delete(self.data, json_path)

    def pop_jsonpath(self, json_path, default=NO_ARGUMENT) \
        -> Union[dict, list, int, str, float]:
        """
        Removes value at jsonpath location, and returns it.
        """

        data = self.get_jsonpath(json_path, default=default)
        self.delete_jsonpath(json_path)
        self.dirty = True
        return data

    def set_jsonpath(self, json_path:str, insert_value:any, overwrite:bool=True):
        """
        Sets value at jsonpath location.

        Can create a new key if it doesn't exist.
        """

        path_exists = self.jsonpath_exists(json_path)

        # If overwrite is false, it will set the path only
        # if there is no path.
        if path_exists and not overwrite:
            return

        # Otherwise, set the value
        self.dirty = True
        dpath.util.new(self.data, json_path, insert_value)
        

    def get_jsonpath(self, json_path, default=NO_ARGUMENT):
        """
        Gets value at jsonpath location.

        A default value may be provided, for missing keys.

        raises:
            AssetNotFoundError if the path does not exist.
        """
        try:
            return dpath.util.get(self.data, json_path)
        except Exception as exception:
            if default is not NO_ARGUMENT:
                return default
            raise AssetNotFoundError(
                f"Path {json_path} does not exist."
            ) from exception

    def get_data_at(self, json_path):
        """
        Returns a list of jsonpaths found at this jsonpath location.
        For a list, this will return: json_path + list index
        For a dict, this will return json_path + dict key

        Exception will be raised if the result is not a list or dict.
        Missing data path will return []
        """
        try:
            # Special case, to handle the root of the json
            if json_path == "**":
                result = self.data
            else:
                result = self.get_jsonpath(json_path, default=[])

            if isinstance(result, dict):
                for key in result.keys():
                    yield json_path + f"/{key}", result[key]
            elif isinstance(result, list):
                for i, element in enumerate(result):
                    yield json_path + f"/[{i}]", element
            else:
                raise AmbiguousAssetError(f"Path '{json_path}' matched a single element, not a list or dict.")

        except KeyError as key_error:
            raise AssetNotFoundError(json_path, self.data) from key_error


class JsonSubResource(JsonResource):
    """
    A sub resource represents a chunk of json data, within a file.
    """
    def __init__(self, parent: Resource = None, json_path: str = None, data: dict = None) -> None:
        super().__init__(data = data, pack = parent.pack, file = parent.file)

        # The parent of the sub-resource is the asset of type Resource
        # which owns this sub-resource. For example a Component is owned by
        # either an EntityFileBP, or a ComponentGroup.
        self.parent: JsonResource = parent

        # The jsonpath is the location within the parent resource, where
        # this sub-resource is stored.
        self._json_path: str = json_path

        # The original path location needs to be stored, for the purpose
        # of renaming or moving the sub-resource.
        self._original_json_path: str = json_path

        # Register self into parent, so that it can be found by the parent
        # during saving, etc.
        self.parent.register_resource(self)
    
    @property
    def json_path(self):
        return self._json_path

    @json_path.setter
    def json_path(self, json_path):
        self.dirty = True
        self._json_path = json_path

    @property
    def id(self):
        """
        The ID of the sub-resource, such as 'minecraft:scale' for a component.
        """
        return self.json_path.rsplit("/", maxsplit=1)[1]

    @id.setter
    def id(self, id):
        self.dirty = True
        self.json_path = self.json_path.rsplit("/", maxsplit=1)[0] + "/" + id

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.id}"

    def __str__(self):
        """
        Returns string representation of this resource.

        The json data will be representation for printing: With the id appended,
        and with indentation.
        """
        return f'"{self.id}": {json.dumps(self.data, indent=2, ensure_ascii=False)}'

    @property
    def dirty(self):
        """
        Returns True if this resource has been modified since it was last saved.
        """
        return self._dirty

    @dirty.setter
    def dirty(self, dirty):
        """
        Set the dirty flag, which stores whether this resource has been
        modified since it was last saved.
        """
        self._dirty = dirty
        self.parent.dirty = dirty # Pseudo recursive call will travel up the chain


    def _save(self):
        """
        Saves the resource, into its parents json structure.

        This works by replacing the data at the jsonpath location,
        meaning that the parent will contain accurate representation of
        the children's data, saved into itself.
        """

        # If the id was updated, we need to serialize into a new location.
        # This implies first deleting the old location, and then creating
        # a new one.
        if not self._deleted:
            if self.json_path != self._original_json_path:
                self.parent.delete_jsonpath(self._original_json_path)
                self.parent.set_jsonpath(self.json_path, self.data)
            else:
                self.parent.set_jsonpath(self.json_path, self.data)

        self._dirty = False

    def _delete(self):
        """
        Deletes itself from parent, by removing the data at the jsonpath
        location.

        If it is a list, it must only set itself to None. The actual
        deletion will take place during saving.
        """
        self.parent.dirty = True
        self.parent._resources.remove(self)
        self._deleted = True
        self.parent.delete_jsonpath(self.json_path)

class JsonFileResource(FileResource, JsonResource):
    """
    A file, which contains json data. Most files in the addon system
    are of this type, or have it as a resource parent.
    """
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        # Init file resource parent, which gives us access to data
        FileResource.__init__(self, file_path=file_path, pack=pack)
        
        # Data is either set directly, or is read from the filepath for this
        # resource. This allows assets to be created from scratch, whilst
        # still having an associated file location.
        if data is not None:
            self.data = data
        else:
            self.data = self.load_json(self.file_path)

        # Init json resource, which relies on the new data attribute
        JsonResource.__init__(self, data=self.data, file=self, pack=pack)

    def load_json(self, local_path: str) -> dict:
        """
        Loads json from file. `local_path` paramater is local to the projects
        input path.
        """
        file_path = os.path.join(self.pack.input_path, local_path)
        if not os.path.exists(file_path):
            raise AssetNotFoundError(f"File not found: {file_path}")
        
        try:
            with open(file_path, "r", encoding='utf8') as fh:
                try:
                    return json.load(fh)
                except json.JSONDecodeError:
                    try:
                        fh.seek(0)
                        contents = ""
                        for line in fh.readlines():
                            cleaned_line = line.split("//", 1)[0]
                            if len(cleaned_line) > 0 and line.endswith("\n") and "\n" not in cleaned_line:
                                cleaned_line += "\n"
                            contents += cleaned_line
                        while "/*" in contents:
                            pre_comment, post_comment = contents.split("/*", 1)
                            contents = pre_comment + post_comment.split("*/", 1)[1]
                        return json.loads(contents)
                    except json.JSONDecodeError as exception:
                        return {}
        except Exception:
            raise InvalidJsonError(file_path)

    def _save(self):
        save_path = os.path.join(self.pack.output_directory, self.file_path)
        create_nested_directory(save_path)

        # If the file has been marked for deletion, delete it
        if self._deleted:
            # If the paths are the same, delete the file, otherwise
            # we can just pass
            if smart_compare(self.pack.input_path, self.pack.output_directory):
                os.remove(save_path)
        else:
            with open(save_path, "w+") as file_head:
                clean_data = {k: v for k, v in self.data.items() if v is not None}
                return json.dump(clean_data, file_head, indent=2, ensure_ascii=False)

class LanguageFile(FileResource):
    """
    A LanguageFile is a language file, such as 'en_US.lang', and is made
    up of many Translations.
    """
    def __init__(self, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(file_path=file_path, pack=pack)
        self.__translations: list[Translation] = []
    
    def get_translation(self, key: str) -> Translation:
        """
        Whether the language file contains the specified key.
        """
        for translation in self.translations:
            if translation.key == key:
                return translation 
        raise AssetNotFoundError(f"Translation with key '{key}' not found in language file '{self.file_path}'.")

    def contains_translation(self, key: str) -> bool:
        """
        Whether the language file contains the specified key.
        """

        for translation in self.translations:
            if translation.key == key:
                return True
        return False

    def delete_translation(self, key: str) -> None:
        """
        Deletes a translation based on key, if it exists.
        """
        for translation in self.translations:
            if translation.key == key:
                self.dirty = True
                self.translations.remove(translation)
                return

    def add_translation(self, translation: Translation, overwrite: bool = True) -> bool:
        """
        Adds a new translation key. Overwrites by default.
        """

        # We must complain about duplicates, unless
        if self.contains_translation(translation.key) and not overwrite:
            return False

        self.dirty = True
        self.__translations.append(translation)

        return True

    def _save(self):
        path = os.path.join(self.pack.output_directory, self.file_path)
        create_nested_directory(path)
        with open(path, 'w', encoding='utf-8') as file:
            for translation in self.translations:
                file.write(f"{translation.key}={translation.value}\t##{translation.comment}\n")


    @cached_property
    def translations(self) -> list[Translation]:
        with open(os.path.join(self.pack.input_path, self.file_path), "r", encoding='utf-8') as language_file:
            for line in language_file.readlines():
                language_regex = "^([^#\n]+?)=([^#]+)#*?([^#]*?)$"
                if match := re.search(language_regex, line):
                    groups = match.groups()
                    self.__translations.append(
                        Translation(
                            key = groups[0].strip() if len(groups) > 0 else "",
                            value = groups[1].strip() if len(groups) > 1 else "",
                            comment = groups[2].strip() if len(groups) > 2 else "",
                        )
                    )
        return self.__translations

# Generic Resources
class Translation():
    """
    Dataclass for a translation. Many translations together make up a
    TranslationFile.
    """

    def __init__(self, key: str, value: str, comment: str = "") -> None:
        self.key = key
        self.value = value
        self.comment = comment

class FormatVersion():
    def __init__(self, version) -> None:
        if isinstance(version, FormatVersion):
            self.major = version.major
            self.minor = version.minor
            self.patch = version.patch
            return
        elif isinstance(version, str):
            elements = version.split('.')
        else:
            # Change to suitable error
            raise TypeError()

        # Pack with extra data if it's missing
        for i in range(3 - len(elements)):
            elements.append('0')
        
        self.major = int(elements[0])
        self.minor = int(elements[1])
        self.patch = int(elements[2])

    def __repr__(self) -> str:
        return f'{self.major}.{self.minor}.{self.patch}'
        
    def __eq__(self, other):
        other = FormatVersion(other)
        return self.major == other.major and self.minor == other.minor and self.patch == other.patch

    def __gt__(self, other):
        if self.major > other.major:
            return True
        elif self.major < other.major:
            return False

        if self.minor > other.minor:
            return True
        elif self.minor < other.minor:
            return False

        if self.patch > other.patch:
            return True
        elif self.patch < other.patch:
            return False
        
        return self != other





### BEHAVIOR PACK

class BehaviorPack(Pack):
    def __init__(self, input_path: str, project: Project = None):
        super().__init__(input_path, project=project)
        self.__functions: FunctionFile = []
        self.__features_file: FeatureFileBP= []
        self.__feature_rules_files: FeatureRuleFile = []
        self.__spawn_rules: SpawnRuleFile = []
        self.__recipes: RecipeFile = []
        self.__entities: EntityFileBP = []
        self.__animation_controller_files: AnimationControllerFileBP = []
        self.__loot_tables: LootTableFile = []
        self.__items: ItemFileBP = []
        self.__blocks: BlockFileBP = []
        # self.function_tick_file: FunctionTickFile = []

    @cached_property
    def functions(self) -> list[FunctionFile]:
        base_directory = os.path.join(self.input_path, "functions")
        for local_path in glob.glob(base_directory + "/**/*.mcfunction", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__functions.append(FunctionFile(file_path = local_path, pack = self))
            
        return self.__functions

    @cached_property
    def feature_files(self) -> list[FeatureFileBP]:
        base_directory = os.path.join(self.input_path, "features")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__features_file.append(FeatureFileBP(file_path = local_path, pack = self))
            
        return self.__features_file

    @cached_property
    def feature_rule_files(self) -> list[FeatureRuleFile]:
        base_directory = os.path.join(self.input_path, "feature_rules")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__feature_rules_files.append(FeatureRuleFile(file_path = local_path, pack = self))
            
        return self.__feature_rules_files

    @cached_property
    def spawn_rules(self) -> list[SpawnRuleFile]:
        base_directory = os.path.join(self.input_path, "spawn_rules")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__spawn_rules.append(SpawnRuleFile(file_path = local_path, pack = self))
            
        return self.__spawn_rules

    @cached_property
    def recipes(self) -> list[RecipeFile]:
        base_directory = os.path.join(self.input_path, "recipes")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__recipes.append(RecipeFile(file_path = local_path, pack = self))
            
        return self.__recipes

    @cached_property
    def entities(self) -> list[EntityFileBP]:
        base_directory = os.path.join(self.input_path, "entities")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__entities.append(EntityFileBP(file_path = local_path, pack = self))
            
        return self.__entities

    @cached_property
    def animation_controller_files(self) -> list[AnimationControllerFileBP]:
        base_directory = os.path.join(self.input_path, "animation_controllers")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__animation_controller_files.append(AnimationControllerFileBP(file_path = local_path, pack = self))
            
        return self.__animation_controller_files

    @cached_property
    def loot_tables(self) -> list[LootTableFile]:
        base_directory = os.path.join(self.input_path, "loot_tables")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__loot_tables.append(LootTableFile(file_path = local_path, pack = self))
            
        return self.__loot_tables

    @cached_property
    def items(self) -> list[ItemFileBP]:
        base_directory = os.path.join(self.input_path, "items")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__items.append(ItemFileBP(file_path = local_path, pack = self))
            
        return self.__items

    @cached_property
    def blocks(self) -> list[BlockFileBP]:
        base_directory = os.path.join(self.input_path, "blocks")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__blocks.append(BlockFileBP(file_path = local_path, pack = self))
            
        return self.__blocks

    def get_function(self, file_path:str) -> FunctionFile:
        """
        Gets a FunctionFile by it's filepath.

        Example: bp.get_function('teleport/home.mcfunction')
        """
        for child in self.functions:
            if smart_compare(child.file_path, file_path):
                return child
        raise AssetNotFoundError(f"Function with path '{file_path}' does not exist.")

    def get_feature_rule_file(self, identifier:str) -> FeatureRuleFile:
        """
        Gets a FeatureRuleFile file by its identifier.

        Example: bp.get_feature_rule_file('reticulator:overworld_underground_tin_ore')
        """
        for child in self.feature_rule_files:
            if smart_compare(child.identifier, identifier):
                return child
        raise AssetNotFoundError(f"FeatureRuleFile with identifier '{identifier}' could not be found.")

    def get_spawn_rule(self, identifier:str) -> SpawnRuleFile:
        """
        Gets a SpawnRuleFile by its identifier.

        Example: bp.get_spawn_rule('reticulator:tin_ore_feature')
        """
        for child in self.spawn_rules:
            if smart_compare(child.identifier, identifier):
                return child
        raise AssetNotFoundError(f"SpawnRuleFile with identifier '{identifier}' could not be found.")

    def get_loot_table(self, file_path:str) -> LootTableFile:
        """
        Gets a LootTableFile by its filepath.

        Example: bp.get_loot_table('entities/boat.json') 
        """
        for child in self.loot_tables:
            if smart_compare(child.file_path, file_path):
                return child
        raise AssetNotFoundError(f"LootTableFile with file_path '{file_path}' could not be found.")

    def get_recipe(self, identifier:str) -> RecipeFile:
        """
        Gets a RecipeFile by its identifier.

        Example: bp.get_recipe('minecraft:acacia_boat') 
        """
        for child in self.recipes:
            if smart_compare(child.identifier, identifier):
                return child
        raise AssetNotFoundError(f"RecipeFile with identifier '{identifier}' could not be found.")

    def get_entity(self, identifier:str) -> EntityFileBP:
        """
        Gets a EntityFileBP by its identifier.

        Example: bp.get_entity('reticulator:lion')
        """
        for child in self.entities:
            if smart_compare(child.identifier, identifier):
                return child
        raise AssetNotFoundError(f"EntityFileBP with identifier '{identifier}' could not be found.")

    def get_item(self, identifier:str) -> ItemFileBP:
        """
        Gets a ItemFileBP by its identifier.

        Example: bp.get_item('reticulator:bronze_sword')
        """
        for item in self.items:
            if smart_compare(item.identifier, identifier):
                return item
        raise AssetNotFoundError(f"ItemFileBP with identifier '{identifier}' could not be found.")

    def get_block(self, identifier:str) -> BlockFileBP:
        """
        Gets a BlockFileBP by its identifier.

        Example: bp.get_block('reticulator:tin')
        """
        for block in self.blocks:
            if smart_compare(block.identifier, identifier):
                return block
        raise AssetNotFoundError(f"BlockFileBP with identifier '{identifier}' could not be found.")


## Behavior Pack SubResources
class Component(JsonSubResource):
    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)


class ComponentGroup(JsonSubResource):
    """
    A component group is a collection of components in an EntityFileBP.
    """
    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)
        self.__components: Component = []

    @cached_property
    def components(self) -> list[Component]:
        for path, data in self.get_data_at("**"):
            self.__components.append(Component(parent = self, json_path = path, data = data))
        return self.__components

    def get_component(self, id:str) -> JsonSubResource:
        """
        Gets a component from this group, by its ID.
        """
        for component in self.components:
            if smart_compare(component.id, id):
                return component
        raise AssetNotFoundError(f"Component called '{id}' could not be found in group '{self.id}'.")

    def add_component(self, name: str, data: dict, overwrite: bool = False) -> Component:
        """
        Adds component to the component group
        """
        self.set_jsonpath(name, data, overwrite)
        new_object = Component(data = data, parent = self, json_path = name)
        self.__components.append(new_object)
        return new_object


class Event(JsonSubResource):
    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)
        
        self.__groups_to_add = []
        self.__groups_to_remove = []

    @cached_property
    def groups_to_add(self) -> list[ComponentGroup]:
        for path, data in self.get_data_at("add/component_groups"):
            self.__groups_to_add.append(ComponentGroup(parent = self, json_path = path, data = data))
        return self.__groups_to_add
    
    @cached_property
    def groups_to_remove(self) -> list[ComponentGroup]:
        for path, data in self.get_data_at("remove/component_groups"):
            self.__groups_to_remove.append(ComponentGroup(parent = self, json_path = path, data = data))
        return self.__groups_to_remove


class LootTablePool(JsonSubResource):
    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)


class Command(Resource):
    """
    A command is a wrapper around a string, which represents a single command
    in a function file.

    To use this class, you can access the 'data' property, and treat it like
    a string.
    """
    def __init__(self, command: str, file: FileResource = None, pack: Pack = None) -> None:
        super().__init__(file=file, pack=pack)

        # The 'data' is the actual command, which is stored as a string.
        self._data: str = command

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data
        self.dirty = True

    @property
    def dirty(self):
        return self._dirty

    @dirty.setter
    def dirty(self, dirty):
        """
        When a command is marked as dirty, it must propagate this to the
        file, so that the file can be marked as dirty.
        """
        self._dirty = dirty
        self.file.dirty = dirty

    def is_comment(self):
        return self.data.startswith("#")

    def __str__(self):
        return self.data

    def __repr__(self):
        return f"Function: '{self.data}'"


## Behavior Pack File Resources

@format_version()
class AnimationControllerFileBP(JsonFileResource):
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)
        self.__animation_controllers = []

    @cached_property
    def animation_controllers(self) -> list[AnimationControllerRP]:
        for path, data in self.get_data_at("animation_controllers"):
            self.__animation_controllers.append(AnimationControllerRP(parent = self, json_path = path, data = data))
        return self.__animation_controllers

    def get_animation_controller(self, id:str) -> AnimationControllerRP:
        for child in self.animation_controllers:
            if smart_compare(child.id, id):
                return child
        raise AssetNotFoundError(id)


@format_version()
@identifier(jsonpath="minecraft:block/description/identifier")
class BlockFileBP(JsonFileResource):
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)
        self.__components: list[JsonSubResource] = []

    @cached_property
    def components(self) -> list[JsonSubResource]:
        for path, data in self.get_data_at("minecraft:block/components"):
            self.__components.append(JsonSubResource(parent = self, json_path = path, data = data))
        return self.__components

    def get_component(self, id:str) -> JsonSubResource:
        for child in self.components:
            if smart_compare(child.id, id):
                return child
        raise AssetNotFoundError(id)


@format_version()
@identifier("minecraft:entity/description/identifier")
class EntityFileBP(JsonFileResource):
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)
        self.__component_groups = []
        self.__components = []
        self.__events = []

    @property
    def counterpart(self) -> EntityFileRP:
        return self.pack.project.resource_pack.get_entity(self.identifier)

    @cached_property
    def component_groups(self) -> list[ComponentGroup]:
        for path, data in self.get_data_at("minecraft:entity/component_groups"):
            self.__component_groups.append(ComponentGroup(parent = self, json_path = path, data = data))
        return self.__component_groups
    
    @cached_property
    def components(self) -> list[Component]:
        for path, data in self.get_data_at("minecraft:entity/components"):
            self.__components.append(Component(parent = self, json_path = path, data = data))
        return self.__components
    
    @cached_property
    def events(self) -> list[Event]:
        for path, data in self.get_data_at("minecraft:entity/events"):
            self.__events.append(Event(parent = self, json_path = path, data = data))
        return self.__events
    
    def get_component_group(self, id:str) -> ComponentGroup:
        for child in self.component_groups:
            if smart_compare(child.id, id):
                return child
        raise AssetNotFoundError(id)

    def get_component(self, id:str) -> Component:
        for child in self.components:
            if smart_compare(child.id, id):
                return child
        raise AssetNotFoundError(id)

    def get_events(self, id:str) -> Event:
        for child in self.events:
            if smart_compare(child.id, id):
                return child
        raise AssetNotFoundError(id)

    @add_sub_resource(cls=ComponentGroup, jsonpath="minecraft:entity/component_groups/", attribute='component_groups')
    def add_component_group(self, *args) -> ComponentGroup:
        """
        Adds component group to the entity components and returns it.
        @param name
        """

    # def add_component_group(self, name: str, data: dict) -> ComponentGroup:
    #     """
    #     Adds a component group to the entity components, and returns it. 
    #     """
    #     self.set_jsonpath("minecraft:entity/component_groups/" + name, data)
    #     new_object = ComponentGroup(data = data, parent = self, json_path = "minecraft:entity/component_groups/" + name)
    #     self.__component_groups.append(new_object)
    #     return new_object

    def add_component(self, name: str, data: dict) -> Component:
        """
        Adds a component to the entity components, and returns it.
        """
        self.set_jsonpath("minecraft:entity/components/" + name, data)
        new_object = Component(data = data, parent = self, json_path="minecraft:entity/components/" + name)
        self.__components.append(new_object)
        return new_object

    def add_event(self, name: str, data: dict) -> Event:
        """
        Adds an event to the entity components, and returns it.
        """
        self.set_jsonpath("minecraft:entity/events/" + name, data)
        new_object = Event(data = data, parent = self, json_path="minecraft:entity/events/" + name)
        self.__events.append(new_object)
        return new_object


@format_version()
class FeatureFileBP(JsonFileResource):
    """
    FeatureFileBP is a JsonFileResource which contains all information about a feature file.
    """
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)


@identifier("minecraft:feature_rules/description/identifier")
@format_version()
class FeatureRuleFile(JsonFileResource):
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)


class FunctionFile(FileResource):
    """
    A FunctionFile is a function file, such as run.mcfunction, and is
    made up of many commands.
    """

    def __init__(self, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(file_path=file_path, pack=pack)
        self.__commands : list[Command] = []
    
    def strip_comments(self):
        """
        Strips all comments from the function file.
        Generally should be used before accessing and using the `commands` property.
        """
        self.commands = [c for c in self.commands if not c.is_comment()]

    @cached_property
    def commands(self) -> list[Command]:
        """
        The list of commands in this function file. Every line represents a Command.
        """
        with open(os.path.join(self.pack.input_path, self.file_path), "r", encoding='utf-8') as function_file:
            for line in function_file.readlines():
                command = line.strip()
                if command:
                    self.__commands.append(Command(command, file=self, pack=self.pack))
        self.__commands = convert_to_notify_structure(self.__commands, self)
        return self.__commands
    
    def _save(self) -> None:
        path = os.path.join(self.pack.output_directory, self.file_path)
        create_nested_directory(path)
        with open(path, 'w', encoding='utf-8') as file:
            for command in self.commands:
                file.write(command.data + '\n')


@format_version()
@identifier("minecraft:item/description/identifier")
class ItemFileBP(JsonFileResource):
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)
        self.__components = []

    @cached_property
    def components(self) -> list[Component]:
        for path, data in self.get_data_at("minecraft:item/components"):
            self.__components.append(Component(parent = self, json_path = path, data = data))
        return self.__components
    
    def get_component(self, id:str) -> Component:
        for child in self.components:
            if smart_compare(child.id, id):
                return child
        raise AssetNotFoundError(id)


class LootTableFile(JsonFileResource):
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)
        self.__pools = []

    @cached_property
    def pools(self) -> list[LootTablePool]:
        for path, data in self.get_data_at("pools"):
            self.__pools.append(LootTablePool(parent = self, json_path = path, data = data))
        return self.__pools


@identifier("**/identifier")
@format_version()
class RecipeFile(JsonFileResource):
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)


@format_version()
@identifier("minecraft:spawn_rules/description/identifier")
class SpawnRuleFile(JsonFileResource):
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)


# class FunctionTickFile(FileResource):
#     def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
#         super().__init__(data = data, file_path = file_path, pack = pack)
#         self.functions = []

### RESOURCE PACK

class ResourcePack(Pack):
    def __init__(self, input_path: str, project: Project = None):
        super().__init__(input_path, project=project)
        self.__particles: list[ParticleFile] = []
        self.__attachables: list[AttachableFileRP] = []
        self.__animation_controller_files: list[AnimationControllerFileRP] = []
        self.__animation_files: list[AnimationControllerFileRP] = []
        self.__entities: list[EntityFileRP] = []
        self.__model_files: list[ModelFile] = []
        self.__models: list[Model] = []
        self.__render_controller_files: list[RenderControllerFile] = []
        self.__items: list[ItemFileRP] = []
        self.__sounds: list[str] = []
        self.__textures: list[str] = []
        self.__material_files: list[MaterialFile] = []
        self.__materials: list[Material] = []
        self.__fogs: list[FogFile] = []
        self.__sounds_file: SoundsFile = None
        self.__sound_definitions_file: SoundDefinitionsFile = None
        self.__terrain_texture_file: StandAloneTextureFile = None
        self.__item_texture_file: StandAloneTextureFile = None
        self.__flipbook_textures_file: FlipbookTexturesFile = None
        self.__blocks_file: BlocksFile = None
        self.__biomes_client_file: BiomesClientFile = None

    # === Cached Properties ===
    @cached_property
    def particles(self) -> list[ParticleFile]:
        base_directory = os.path.join(self.input_path, "particles")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__particles.append(ParticleFile(file_path = local_path, pack = self))
            
        return self.__particles

    @cached_property
    def attachables(self) -> list[AttachableFileRP]:
        base_directory = os.path.join(self.input_path, "attachables")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__attachables.append(AttachableFileRP(file_path = local_path, pack = self))
            
        return self.__attachables

    @cached_property
    def animation_controller_files(self) -> list[AnimationControllerFileRP]:
        base_directory = os.path.join(self.input_path, "animation_controllers")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__animation_controller_files.append(AnimationControllerFileRP(file_path = local_path, pack = self))
            
        return self.__animation_controller_files

    @cached_property
    def animation_files(self) -> list[AnimationFileRP]:
        base_directory = os.path.join(self.input_path, "animations")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__animation_files.append(AnimationFileRP(file_path = local_path, pack = self))
            
        return self.__animation_files

    @cached_property
    def material_files(self) -> list[MaterialFile]:
        base_directory = os.path.join(self.input_path, "materials")
        for local_path in glob.glob(base_directory + "/**/*.material", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__material_files.append(MaterialFile(file_path = local_path, pack = self))
        return self.__material_files

    @cached_property
    def entities(self) -> list[EntityFileRP]:
        base_directory = os.path.join(self.input_path, "entity")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__entities.append(EntityFileRP(file_path = local_path, pack = self))
        return self.__entities

    @cached_property
    def fogs(self) -> list[FogFile]:
        base_directory = os.path.join(self.input_path, "fogs")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__fogs.append(FogFile(file_path = local_path, pack = self))
        return self.__fogs

    @cached_property
    def model_files(self) -> list[ModelFile]:
        base_directory = os.path.join(self.input_path, "models")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__model_files.append(ModelFile(file_path = local_path, pack = self))
            
        return self.__model_files

    @cached_property
    def render_controller_files(self) -> list[RenderControllerFile]:
        base_directory = os.path.join(self.input_path, "render_controllers")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__render_controller_files.append(RenderControllerFile(file_path = local_path, pack = self))
            
        return self.__render_controller_files

    @cached_property
    def items(self) -> list[ItemFileRP]:
        base_directory = os.path.join(self.input_path, "items")
        for local_path in glob.glob(base_directory + "/**/*.json", recursive=True):
            local_path = os.path.relpath(local_path, self.input_path)
            self.__items.append(ItemFileRP(file_path = local_path, pack = self))
            
        return self.__items

    @cached_property
    def animations(self) -> list[AnimationRP]:
        children = []
        for file in self.animation_files:
            for child in file.animations:
                children.append(child)
        return children

    @cached_property
    def render_controllers(self) -> list[RenderController]:
        children = []
        for file in self.render_controller_files:
            for child in file.render_controllers:
                children.append(child)
        return children

    @cached_property
    def animation_controllers(self) -> list[AnimationControllerRP]:
        children = []
        for file in self.animation_controller_files:
            for child in file.animation_controllers:
                children.append(child)
        return children

    @cached_property
    def models(self) -> list[Model]:
        for file in self.model_files:
            for child in file.models:
                self.__models.append(child)
        return self.__models

    @cached_property
    def materials(self) -> list[Material]:
        for file in self.material_files:
            for child in file.materials:
                self.__materials.append(child)
        return self.__materials

    @cached_property
    def sounds(self) -> list[str]:
        """
        Returns a list of all sounds in the pack, relative to the pack root.
        """
        glob_pattern = os.path.join(self.input_path, "sounds") + "/**/*."
        for extension in SOUND_EXTENSIONS:
            self.__sounds.extend(glob.glob(glob_pattern + extension, recursive=True))

        self.__sounds = [os.path.relpath(path, self.input_path).replace(os.sep, '/') for path in self.__sounds]
        return self.__sounds

    def get_sounds(self, search_path: str = "", trim_extension: bool = True) -> list[str]:
        """
        Returns a list of all child sounds of the searchpath, relative to the pack root. 
        Search path should not include 'sounds'.

        You may optionally trim the extension from the returned paths.

        Example: rp.get_sounds("entities", trim_extension=True)
        """
        sounds = []
        glob_pattern = os.path.join(self.input_path, "sounds", search_path) + "/**/*."
        for extension in SOUND_EXTENSIONS:
            sounds.extend(glob.glob(glob_pattern + extension, recursive=True))

        sounds = [os.path.relpath(path, self.input_path).replace(os.sep, '/') for path in sounds]
        if trim_extension:
            sounds = [os.path.splitext(path)[0] for path in sounds]
        return sounds
    
    @cached_property
    def textures(self) -> list[str]:
        """
        Returns a list of all textures in the pack, relative to the pack root.

        Example: "textures/my_texture.png"
        """
        glob_pattern = os.path.join(self.input_path, "textures") + "/**/*."
        for extension in TEXTURE_EXTENSIONS:
            self.__textures.extend(glob.glob(glob_pattern + extension, recursive=True)) 

        self.__textures = [os.path.relpath(path, self.input_path).replace(os.sep, '/') for path in self.__textures]
        return self.__textures
    
    def get_textures(self, search_path: str = "", trim_extension: bool = True) -> list[str]:
        """
        Returns a list of all child textures of the searchpath, relative to the pack root. 
        Search path should not include 'textures'.

        You may optionally trim the extension from the returned paths.

        Example: rp.get_textures("entities", trim_extension=True)
        """
        textures = []
        glob_pattern = os.path.join(self.input_path, "textures", search_path) + "/**/*."
        for extension in TEXTURE_EXTENSIONS:
            textures.extend(glob.glob(glob_pattern + extension, recursive=True))

        textures = [os.path.relpath(path, self.input_path).replace(os.sep, '/') for path in textures]
        if trim_extension:
            textures = [os.path.splitext(path)[0] for path in textures]
        return textures

    # === Individual Files ===
    @cached_property
    def sounds_file(self) -> SoundsFile:
        file_path = "sounds.json"
        self.__sounds_file = SoundsFile(file_path = file_path, pack = self)
        return self.__sounds_file

    @cached_property
    def sound_definitions_file(self) -> SoundDefinitionsFile:
        file_path = os.path.join("sounds", "sound_definitions.json")
        self.__sound_definitions_file = SoundDefinitionsFile(file_path = file_path, pack = self)
        return self.__sound_definitions_file

    @cached_property
    def terrain_texture_file(self) -> StandAloneTextureFile:
        file_path = os.path.join("textures", "terrain_texture.json")
        self.__terrain_texture_file = StandAloneTextureFile(file_path = file_path, pack = self)
        return self.__terrain_texture_file

    @cached_property
    def item_texture_file(self) -> StandAloneTextureFile:
        file_path = os.path.join("textures", "item_texture.json")
        self.__item_texture_file = StandAloneTextureFile(file_path = file_path, pack = self)
        return self.__item_texture_file

    @cached_property
    def flipbook_textures_file(self) -> FlipbookTexturesFile:
        file_path = os.path.join("textures", "flipbook_textures.json")
        self.__flipbook_textures_file = FlipbookTexturesFile(file_path = file_path, pack = self)
        return self.__flipbook_textures_file

    @cached_property
    def blocks_file(self) -> BlocksFile:
        file_path = "blocks.json"
        self.__blocks_file = BlocksFile(file_path = file_path, pack = self)
        return self.__blocks_file

    @cached_property
    def biomes_client_file(self) -> BiomesClientFile:
        file_path = "biomes_client.json"
        self.__biomes_client_file = BiomesClientFile(file_path = file_path, pack = self)
        return self.__biomes_client_file

    # === Getters ===
    def get_particle(self, identifier:str) -> ParticleFile:
        for child in self.particles:
            if smart_compare(child.identifier, identifier):
                return child
        raise AssetNotFoundError(identifier)

    def get_fog(self, identifier:str) -> FogFile:
        for fog in self.fogs:
            if smart_compare(fog.identifier, identifier):
                return fog
        raise AssetNotFoundError(f"Fog with identifier {identifier} could not be found.")


    def get_attachable(self, identifier:str) -> AttachableFileRP:
        """
        Gets an AttachableFileRP by its identifier.

        Example: get_attachable("reticulator:sabatons")
        """
        for attachable in self.attachables:
            if smart_compare(attachable.identifier, identifier):
                return attachable
        raise AssetNotFoundError(f"Attachable with identifier '{identifier}' not does not exist.")

    def get_animation_controller_file(self, file_path:str) -> AnimationControllerFileRP:
        """
        Gets the AnimationControllerFileRP with the given path.

        Example: get_animation_controller_file("example.json")
        """
        for acf in self.animation_controller_files:
            if smart_compare(acf.file_path, file_path):
                return acf
        raise AssetNotFoundError(f"AnimationControllerFileRP with path '{file_path}' does not exist.")

    def get_material_file(self, file_path:str) -> MaterialFile:
        for material_file in self.material_files:
            if smart_compare(material_file.file_path, file_path):
                return material_file
        raise AssetNotFoundError(f"MaterialFile with path '{file_path}' does not exist.")

    def get_material(self, id:str) -> Material:
        for file_child in self.material_files:
            for child in file_child.materials:
                if smart_compare(child.id, id):
                    return child
        raise AssetNotFoundError(f"MaterialRP with id '{id}' does not exist.")

    def get_animation_file(self, file_path:str) -> AnimationFileRP:
        """
        Gets the AnimationFileRP with the given path.

        Example: get_animation_file("example.json")
        """
        
        for child in self.animation_files:
            if smart_compare(child.file_path, file_path):
                return child
        raise AssetNotFoundError(f"AnimationFileRP with path '{file_path}' does not exist.")

    def get_entity(self, identifier:str) -> EntityFileRP:
        """
        Gets the EntityFileRP with the given identifier.

        Example: get_entity("reticulator:walrus")
        """

        for child in self.entities:
            if smart_compare(child.identifier, identifier):
                return child
        raise AssetNotFoundError(f"Entity with identifier '{identifier}' does not exist.")

    def get_model_file(self, file_path:str) -> ModelFile:
        """
        Gets the ModelFile with the given path.

        Example: get_model_file("example.json")
        """
        
        for model_file in self.model_files:
            if smart_compare(model_file.file_path, file_path):
                return model_file
        raise AssetNotFoundError(f"ModelFile with path '{file_path}' does not exist.")

    def get_render_controller_file(self, file_path:str) -> RenderControllerFile:
        """
        Gets the RenderControllerFile with the given path.
        
        Example: get_render_controller_file("example.json")
        """

        for child in self.render_controller_files:
            if smart_compare(child.file_path, file_path):
                return child
        raise AssetNotFoundError(f"RenderControllerFile with path '{file_path}' does not exist.")

    def get_animation(self, id:str) -> AnimationRP:
        """
        Gets the AnimationRP with the given id, by searching through all animation files.

        Example: get_animation("animation.parrot.idle")
        """

        for file_child in self.animation_files:
            for child in file_child.animations:
                if smart_compare(child.id, id):
                    return child
        raise AssetNotFoundError(f"Animation with id '{id}' does not exist.")

    def get_render_controller(self, id:str) -> RenderController:
        """
        Gets the RenderControllerRP with the given id, by searching through all render controller files.

        Example: get_render_controller("controller.render.wooly_mammoth")
        """

        for file_child in self.render_controller_files:
            for child in file_child.render_controllers:
                if smart_compare(child.id, id):
                    return child
        raise AssetNotFoundError(f"RenderController with id '{id}' does not exist.")

    def get_animation_controller(self, id:str) -> AnimationControllerRP:
        for file_child in self.animation_controller_files:
            for child in file_child.animation_controllers:
                if smart_compare(child.id, id):
                    return child
        raise AssetNotFoundError(id)

    def get_model(self, identifier:str) -> Model:
        for file_child in self.model_files:
            for child in file_child.models:
                if smart_compare(child.identifier, identifier):
                    return child
        raise AssetNotFoundError(identifier)


## Resource Pack File Resources
class AnimationControllerFileRP(JsonFileResource):
    """
    AnimationControllerFileRP
    """
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)
        self.__animation_controllers = []

    @cached_property
    def animation_controllers(self) -> list[AnimationControllerRP]:
        for path, data in self.get_data_at("animation_controllers"):
            self.__animation_controllers.append(AnimationControllerRP(parent = self, json_path = path, data = data))
        return self.__animation_controllers

    def get_animation_controller(self, id:str) -> AnimationControllerRP:
        for child in self.animation_controllers:
            if smart_compare(child.id, id):
                return child
        raise AssetNotFoundError(id)


class AnimationRP(JsonSubResource):
    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)
        self.__bones = []

    @sub_resource(cls=JsonSubResource, jsonpath='bones')
    def bones(self) -> list[JsonSubResource]: pass
    
    @property
    def loop(self):
        return self.get_jsonpath("loop")
    
    @loop.setter
    def loop(self, loop):
        return self.set_jsonpath("loop", loop)

class AnimationFileRP(JsonFileResource):
    """
    AnimationFileRP is a class which represents a resource pack's animation file.
    Since many animations are defined in the same file, it is often more useful.
    to use the AnimationRP class instead.
    """
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)
    
    @sub_resource(cls=AnimationRP, jsonpath='animations')
    def animations(self) -> list[AnimationRP]: pass

    @get_sub_resource('animations', 'id')
    def get_animation(self, id: str) -> AnimationRP: pass

    @add_sub_resource(cls=AnimationRP, jsonpath="animations/", attribute='animations')
    def add_component_group(self, *args) -> AnimationRP: pass


@format_version()
@identifier("minecraft:attachable/description/identifier")
class AttachableFileRP(JsonFileResource):
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)

class BiomesClientFile(JsonFileResource):
    """
    BiomesClientFile is a class which represents the data stored in 'rp/biomes_client.json'
    """
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)


class BlocksFile(JsonFileResource):
    """
    BlocksFile is a class which represents the data stored in 'rp/blocks.json'
    """
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)


@format_version()
@identifier("minecraft:client_entity/description/identifier")
class EntityFileRP(JsonFileResource):
    """
    EntityFileRP is a class which represents a resource pack's entity file.
    """
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)
        self.__animations: AnimationTriple = []
        self.__models: ModelTriple = []
        self.__textures: TextureDouble = []
        self.__materials: MaterialTriple = []

    @property
    def counterpart(self) -> EntityFileBP:
        return self.pack.project.behavior_pack.get_entity(self.identifier)

    @cached_property
    def animations(self) -> list[AnimationTriple]:
        for path, data in self.get_data_at("minecraft:client_entity/description/animations"):
            self.__animations.append(AnimationTriple(parent = self, json_path = path, data = data))
        return self.__animations
    
    def get_animation(self, identifier:str) -> AnimationTriple:
        """
        Fetches an AnimationTriple resource, either by shortname, or identifier.
        """
        for child in self.animations:
            if smart_compare(child.shortname, identifier) or smart_compare(child.identifier, identifier):
                return child
        raise AssetNotFoundError(id)

    @cached_property
    def textures(self) -> list[TextureDouble]:
        for path, data in self.get_data_at("minecraft:client_entity/description/textures"):
            self.__textures.append(TextureDouble(parent = self, json_path = path, data = data))
        return self.__textures
    
    def get_texture(self, identifier:str) -> TextureDouble:
        """
        Fetches a texture resource, either by shortname, or texture_path.
        """
        for child in self.textures:
            if smart_compare(child.shortname, identifier) or smart_compare(child.texture_path, identifier):
                return child
        raise AssetNotFoundError(id)

    @cached_property
    def models(self) -> list[ModelTriple]:
        for path, data in self.get_data_at("minecraft:client_entity/description/geometry"):
            self.__models.append(ModelTriple(parent = self, json_path = path, data = data))
        return self.__models
    
    def get_model(self, identifier:str) -> ModelTriple:
        """
        Fetches a model resource, either by shortname, or identifier.
        """
        for child in self.models:
            if smart_compare(child.shortname, identifier) or smart_compare(child.identifier, identifier):
                return child
        raise AssetNotFoundError(id)

    @cached_property
    def materials(self) -> list[MaterialTriple]:
        for path, data in self.get_data_at("minecraft:client_entity/description/materials"):
            self.__materials.append(MaterialTriple(parent = self, json_path = path, data = data))
        return self.__materials
    
    def get_material(self, identifier:str) -> MaterialTriple:
        """
        Fetches a material resource, either by shortname, or material type.
        """
        for child in self.materials:
            if smart_compare(child.shortname, identifier) or smart_compare(child.identifier, identifier):
                return child
        raise AssetNotFoundError(id)


class FlipbookTexturesFile(JsonFileResource):
    """
    FlipbookTexturesFile is a class which represents the data stored in 'rp/textures/flipbook_textures.json'
    """
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)


@format_version()
@identifier("minecraft:fog_settings/description/identifier")
class FogFile(JsonFileResource):
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)
        self.__distance_components: list[Component] = []
        self.__volumetric_density_components: list[Component] = []
        self.__volumetric_media_coefficients: list[Component] = []

    @cached_property
    def distance_components(self) -> list[Component]:
        for path, data in self.get_data_at("minecraft:fog_settings/distance"):
            self.__distance_components.append(Component(parent = self, json_path = path, data = data))
        return self.__distance_components

    @cached_property
    def volumetric_density_components(self) -> list[Component]:
        for path, data in self.get_data_at("minecraft:fog_settings/volumetric/density"):
            self.__volumetric_density_components.append(Component(parent = self, json_path = path, data = data))
        return self.__volumetric_density_components

    @cached_property
    def volumetric_media_coefficients(self) -> list[Component]:
        for path, data in self.get_data_at("minecraft:fog_settings/volumetric/media_coefficients"):
            self.__volumetric_media_coefficients.append(Component(parent = self, json_path = path, data = data))
        return self.__volumetric_media_coefficients

    def get_distance_component(self, id:str) -> Component:
        for child in self.distance_components:
            if smart_compare(child.id, id):
                return child
        raise AssetNotFoundError(f"Distance component with id '{id}' not found.")

    def get_volumetric_density_component(self, id:str) -> Component:
        for child in self.distance_components:
            if smart_compare(child.id, id):
                return child
        raise AssetNotFoundError(f"Volumetric density component with id '{id}' not found.")

    def get_volumetric_media_coefficient(self, id:str) -> Component:
        for child in self.volumetric_media_coefficients:
            if smart_compare(child.id, id):
                return child
        raise AssetNotFoundError(f"volumetric media coefficient component with id '{id}' not found.")

@format_version()
@identifier("minecraft:item/description/identifier")
class ItemFileRP(JsonFileResource):
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)
        self.__components: Component = []

    @cached_property
    def components(self) -> list[JsonSubResource]:
        for path, data in self.get_data_at("minecraft:item/components"):
            self.__components.append(JsonSubResource(parent = self, json_path = path, data = data))
        return self.__components
    
    def get_component(self, id:str) -> JsonSubResource:
        for child in self.components:
            if smart_compare(child.id, id):
                return child
        raise AssetNotFoundError(id)


## TODO: These files contain format version in field version/format

@format_version(jsonpath="materials/version")
class MaterialFile(JsonFileResource):
    """
    MaterialFile is a class which represents a resource pack's material file.
    Since many materials can be defined in the same file, it is often more useful
    to use the MaterialRP class directly.
    """
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)
        self.__materials: Material = []

    # TODO: Shouldn't this be only returning for stuff found within materials?
    # It also should be sorting out the 'version' key.
    @cached_property
    def materials(self) -> list[Material]:
        for path, data in self.get_data_at("**"):
            self.__materials.append(Material(parent = self, json_path = path, data = data))
        return self.__materials

@format_version()
class ModelFile(JsonFileResource):
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)
        self.__models = []

    @cached_property
    def models(self) -> list[Model]:
        for path, data in self.get_data_at("minecraft:geometry"):
            self.__models.append(Model(parent = self, json_path = path, data = data))
        return self.__models

@format_version()
@identifier("particle_effect/description/identifier")
class ParticleFile(JsonFileResource):
    """
    ParticleFile is a JsonFileResource which represents a particle file.
    """
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)
        self.__components: JsonSubResource = []
        self.__events: JsonSubResource = []

    @cached_property
    def components(self) -> list[JsonSubResource]:
        for path, data in self.get_data_at("particle_effect/components"):
            self.__components.append(JsonSubResource(parent = self, json_path = path, data = data))
        return self.__components
    
    @cached_property
    def events(self) -> list[JsonSubResource]:
        for path, data in self.get_data_at("particle_effect/events"):
            self.__events.append(JsonSubResource(parent = self, json_path = path, data = data))
        return self.__events

    def get_component(self, id:str) -> JsonSubResource:
        """
        Gets a specific JsonSubResource component from the particle.

        Example: particle.get_component('minecraft:particle_motion_dynamic')
        """
        for component in self.components:
            if smart_compare(component.id, id):
                return component
        raise AssetNotFoundError(f"Component called '{id}' could not be found on {self.identifier}.")

    def get_event(self, id:str) -> JsonSubResource:
        """
        Gets a specific JsonSubResource event from the particle.

        Example: particle.get_event('my_event')
        """
        for event in self.events:
            if smart_compare(event.id, id):
                return event
        raise AssetNotFoundError(f"Event called '{id}' could not be found on {self.identifier}.")


class RenderController(JsonSubResource):
    """
    A JsonSubResource, representing a single Render Controller object, contained
    within a RenderControllerFile.
    """

    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)

@format_version()
class RenderControllerFile(JsonFileResource):
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)
        self.format_version : FormatVersion

    @sub_resource(cls=RenderController, jsonpath='render_controllers')
    def render_controllers(self) -> list[RenderController]: pass
    
    @get_sub_resource('render_controllers', 'id')
    def get_render_controller(self, id: str) -> RenderController: pass

@format_version()
class SoundDefinitionsFile(JsonFileResource):
    """
    SoundsDefinitionFile is a class which represents the data stored in
    'rp/sounds/sound_definitions.json'
    """
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data, file_path, pack)
        self.format_version : FormatVersion

# TODO: Allow accessing child sounds here
class SoundsFile(JsonFileResource):
    """
    SoundsFile is a class which represents the data stored in 'rp/sounds.json'
    """
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)


class StandAloneTextureFile(JsonFileResource):
    """
    StandAloneTextureFile is a class which represents the data stored in 'rp/textures/*_texture.json'
    style files.
    """
    def __init__(self, data: dict = None, file_path: str = None, pack: Pack = None) -> None:
        super().__init__(data = data, file_path = file_path, pack = pack)
        self.__texture_definitions = []
    
    @cached_property
    def texture_definitions(self) -> list[TextureFileDouble]:
        for path, data in self.get_data_at("texture_data"):
            self.__texture_definitions.append(TextureFileDouble(parent = self, json_path = path, data = data))
        return self.__texture_definitions

    def get_texture_definition(self, shortname: str) -> TextureFileDouble:
        for child in self.texture_definitions:
            if child.shortname == shortname:
                return child
        raise AssetNotFoundError(f"Texture definition for shortname '{shortname}' not found.")

    def add_texture_definition(self, shortname: str, textures: list[str]):
        self.set_jsonpath(f"texture_data/{shortname}", {
            "textures": textures
        })
        self.__texture_definitions.append(TextureFileDouble(parent = self, json_path = f"texture_data/{shortname}", data = {"textures": textures}))

## Resource Pack SubResources

class Material(JsonSubResource):
    """
    Represents a single material, from a .material file
    """
    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)


class MaterialTriple(JsonSubResource):
    """
    A special sub-resource, which represents a material within an RP entity.
    """
    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)

    @property
    def shortname(self):
        return self.id

    @shortname.setter
    def shortname(self, shortname):
        self.id = shortname
    
    @property
    def identifier(self):
        return self.data
    
    @identifier.setter
    def identifier(self, identifier):
        self.data = identifier

    @cached_property
    def resource(self):
        return self.parent.pack.get_material(self.identifier)
    
    def exists(self):
        try:
            self.parent.pack.get_material(self.identifier)
            return True
        except AssetNotFoundError:
            return False





class AnimationTriple(JsonSubResource):
    """
    A special sub-resource, which represents an animation within an RP entity.
    """
    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)

    @property
    def shortname(self):
        return self.id

    @shortname.setter
    def shortname(self, shortname):
        self.id = shortname
    
    @property
    def identifier(self):
        return self.data
    
    @identifier.setter
    def identifier(self, identifier):
        self.data = identifier

    @cached_property
    def resource(self):
        return self.parent.pack.get_animation(self.identifier)
    
    def exists(self):
        """
        Whether the animation described by this triple exists.
        Can be used to detect if a entity is referencing a missing animation.
        """
        try:
            self.parent.pack.get_animation(self.identifier)
            return True
        except AssetNotFoundError:
            return False


class AnimationControllerRP(JsonSubResource):
    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)
        
        self.__states = []

    @cached_property
    def states(self) -> list[AnimationControllerStateRP]:
        for path, data in self.get_data_at("states"):
            self.__states.append(AnimationControllerStateRP(parent = self, json_path = path, data = data))
        return self.__states
    
    @property
    def initial_state(self):
        return self.get_jsonpath("initial_state")
    
    @initial_state.setter
    def initial_state(self, initial_state):
        return self.set_jsonpath("initial_state", initial_state)

    def get_state(self, id:str) -> AnimationControllerStateRP:
        for child in self.states:
            if smart_compare(child.id, id):
                return child
        raise AssetNotFoundError(id)


class AnimationControllerStateRP(JsonSubResource):
    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)


class Cube(JsonSubResource):
    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)


class Bone(JsonSubResource):
    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)
        
        self.__cubes = []
    
    @property
    def name(self):
        return self.get_jsonpath("name")
    
    @name.setter
    def identifier(self, name):
        return self.set_jsonpath("name", name)

    @cached_property
    def cubes(self) -> list[Cube]:
        for path, data in self.get_data_at("cubes"):
            self.__cubes.append(Cube(parent = self, json_path = path, data = data))
        return self.__cubes


@identifier("description/identifier")
class Model(JsonSubResource):
    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)
        
        self.__bones = []
        
    @cached_property
    def bones(self) -> list[Bone]:
        for path, data in self.get_data_at("bones"):
            self.__bones.append(Bone(parent = self, json_path = path, data = data))
        return self.__bones
    
    def get_bone(self, name:str) -> Bone:
        """
        Gets a Bone via its name field.
        """
        for bone in self.bones:
            if smart_compare(bone.name, name):
                return bone
        raise AssetNotFoundError(f"Bone with name {name} not found.")


class ModelTriple(JsonSubResource):
    """
    A special sub-resource, which represents a model within an RP entity.
    """
    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)

    @property
    def shortname(self):
        return self.id

    @shortname.setter
    def shortname(self, shortname):
        self.id = shortname
    
    @property
    def identifier(self):
        return self.data
    
    @identifier.setter
    def identifier(self, identifier):
        self.data = identifier

    @cached_property
    def resource(self):
        return self.parent.pack.get_model(self.identifier)
    
    def exists(self):
        """
        Whether the model described by this triple exists.
        Can be used to detect if a entity is referencing a missing model.
        """
        try:
            self.parent.pack.get_model(self.identifier)
            return True
        except AssetNotFoundError:
            return False


class TextureDouble(JsonSubResource):
    """
    A special sub-resource, which represents a texture within an RP entity.
    """
    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)

    @property
    def shortname(self):
        return self.id

    @shortname.setter
    def shortname(self, shortname):
        self.id = shortname
    
    @property
    def texture_path(self):
        return self.data
    
    @texture_path.setter
    def texture_path(self, texture_path):
        self.data = texture_path
    
    def exists(self) -> bool:
        """
        Returns True if this resource exists in the pack.
        """
        return os.path.exists(os.path.join(self.pack.input_path, self.file_path))


class TextureFileDouble(JsonSubResource):
    """
    A special sub-resource, which represents a texture within a texture
    definition file, such as 'item_texture.json'

    This is a special case, as it has some additional logic for obscuring the
    texture path. This is because textures are stored nested under 
    'textures' which is simply inconvenient to work with.
    """

    def __init__(self, data: dict = None, parent: Resource = None, json_path: str = None ) -> None:
        super().__init__(data=data, parent=parent, json_path=json_path)
 
        self.textures = data.get("textures", [])
        if not isinstance(self.textures, list):
            self.textures = [self.textures]
        
        self.textures = convert_to_notify_structure(self.textures, self)
        
    @property
    def shortname(self):
        return self.id

    @shortname.setter
    def shortname(self, shortname):
        self.id = shortname
    
    @property
    def data(self):
        """
        Custom data getter allows us to re-create the json structure based
        on the saved textures.
        """
        return {
            "textures": self.textures
        }
