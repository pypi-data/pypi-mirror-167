class StructureNotEqualError(ValueError):
    pass


class StructureOverlapError(ValueError):
    pass


class GridNotEqualError(ValueError):
    pass


class AnimationError(RuntimeError):
    pass


class FrequencyError(IndexError):
    pass


class AttributeNotRegisteredError(AttributeError):
    pass


class AttributeNotAssignedError(AttributeError):
    pass


class XSDFileNotFoundError(FileNotFoundError):
    pass


class TooManyXSDFileError(FileExistsError):
    pass


class ParameterError(TypeError):
    pass


class JsonFileNotFoundError(FileNotFoundError):
    pass


class PotDirNotExistError(FileExistsError):
    pass


class ConstrainError(TypeError):
    pass


class PathNotExistError(TypeError):
    pass
