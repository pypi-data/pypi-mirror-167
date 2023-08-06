"""
Windows Registry Terminology:

KEY - like a folder
VALUE - like a file, has a name, a type and a value (for want of a better word)

Keys and values are case insensitive.
"""
import winreg
from pathlib import Path

__version__   = "1.0.0rc1"
__author__    = "Adam Kerz"
__copyright__ = "Copyright (C) 2016-22 Adam Kerz"


__ALL__=['RegPath','RegValue']


# ----------------------------------------
# Helper functions
# ----------------------------------------
def _ignore_file_not_found_error(fn,finallyFn=None):
    """Tries to execute fn and returns None if it raises a FileNotFoundError: [WinError 2]. Raises all other exceptions. Optional function to call on finally."""
    try:
        return fn()
    except OSError as e:
        # FileNotFoundError
        if e.winerror==2: return None
        raise
    finally:
        if callable(finallyFn): finallyFn()

def _open_key(reg_path,access=winreg.KEY_READ,error_on_non_existent=True):
    """Tries to open the key with the given security access and returns a winreg.handle object. Errors if not found, unless error_on_non_existent is True, in which case None is returned."""
    fn=lambda: winreg.OpenKey(reg_path.hkey_constant,reg_path.path,0,access)
    if error_on_non_existent: return fn()
    return _ignore_file_not_found_error(fn)



# ----------------------------------------
# RegPath class
# ----------------------------------------
class RegPath(object):
    """Represents a particular path in the registry."""

    HKEY_CONSTANTS={
        'HKEY_CURRENT_USER':winreg.HKEY_CURRENT_USER,
        'HKEY_LOCAL_MACHINE':winreg.HKEY_LOCAL_MACHINE,
        'HKEY_CLASSES_ROOT':winreg.HKEY_CLASSES_ROOT,
        'HKEY_USERS':winreg.HKEY_USERS,
        'HKEY_CURRENT_CONFIG':winreg.HKEY_CURRENT_CONFIG,
    }
    HKEY_CONSTANTS_SHORT={
        'HKCU':winreg.HKEY_CURRENT_USER,
        'HKLM':winreg.HKEY_LOCAL_MACHINE,
        'HKCR':winreg.HKEY_CLASSES_ROOT,
        'HKU':winreg.HKEY_USERS,
        'HKCC':winreg.HKEY_CURRENT_CONFIG,
    }
    HKEY_CONSTANTS.update(HKEY_CONSTANTS_SHORT)
    HKEYS={value:key for key,value in HKEY_CONSTANTS.items()}
    for key,value in HKEY_CONSTANTS_SHORT.items(): HKEYS[value]=key
    UNSET_VALUE=object()


    # ----------------------------------------
    # Construction
    # ----------------------------------------
    def __init__(self,path,hkey_constant=None):
        # accept RegPath objects
        if isinstance(path,RegPath):
            self.hkey_constant=hkey_constant if hkey_constant else path.hkey_constant
            self.path=path.path
        else:
            # and strings
            path.rstrip('\\')
            if hkey_constant:
                self.hkey_constant=hkey_constant
                self.path=path
            else:
                self.hkey_constant,self.path=self._split_path(path)


    def __truediv__(self,path):
        """
        Creates a new reg path by appending the given path component.

            p=RegPath('HKCU\\Software')/'longer'
            assert p.name=='longer'
        """
        return RegPath(self.path+'\\'+path,self.hkey_constant)


    # ----------------------------------------
    # properties
    # ----------------------------------------
    # TODO: cache results of these functions - path objects should be considered immutable
    @property
    def hkey(self):
        """Short string version of this path's HKEY."""
        return self.HKEYS[self.hkey_constant]

    @property
    def name(self):
        """The key name."""
        return self.path.rsplit('\\',1)[-1]

    @property
    def parent(self):
        """A `RegPath` object that is the parent of this key."""
        return RegPath(self.path.rsplit('\\',1)[0],self.hkey_constant)


    # ----------------------------------------
    # Key manipulation
    # ----------------------------------------
    def exists(self):
        """Returns True if the key exists."""
        # open (and then close) the key to see if it exists
        try:
            handle=_open_key(self)
        except OSError as e:
            if e.winerror==2: return False
            raise
        else:
            handle.Close()
            return True


    def create(self):
        """Ensures the key (and all parent keys) exist, creating them if they don't."""
        # this either creates the key (and all parent keys) if it doesn't exist or just opens the handle if it does
        handle=winreg.CreateKey(self.hkey_constant,self.path)
        handle.Close()


    def delete(self,recurse=False):
        """Deletes an existing key and any values it has. Will only delete subkeys if `recurse` is True otherwise will error."""
        # delete subkeys if recurse
        if recurse:
            for k in self.subkeys():
                k.delete(recurse=True)
        # then delete this key, ignoring it not existing
        handle=_open_key(self.parent,error_on_non_existent=False)
        if not handle: return
        _ignore_file_not_found_error(lambda:winreg.DeleteKey(handle,self.name),finallyFn=lambda:handle.Close())


    def subkeys(self):
        """A generator that yields a `RegPath` for each subkey in this key"""
        # open the key and make sure it exists
        handle=_open_key(self)
        try:
            # iterate until an exception is raised, telling us we have no more data
            i=0
            while True:
                yield self/winreg.EnumKey(handle,i)
                i+=1
        except OSError as e:
            # 259=No more data is available
            if e.winerror==259: return
            raise
        finally:
            handle.Close()


    def subvalues(self):
        """A generator that yields a `RegValue` for each subvalue in this key"""
        # open the key and make sure it exists
        handle=_open_key(self)
        try:
            # iterate until an exception is raised, telling us we have no more data
            i=0
            while True:
                (name,value,type)=winreg.EnumValue(handle,i)
                # TODO: value and type aren't cached in the RegValue class
                v=RegValue(self,name)
                yield v
                i+=1
        except OSError as e:
            # 259=No more data is available
            if e.winerror==259: return
            raise
        finally:
            handle.Close()


    # ----------------------------------------
    # Value manipulation
    # ----------------------------------------
    def value(self,name):
        """Returns a `RegValue` object for the value `name` at this path."""
        return RegValue(self,name)


    # ----------------------------------------
    # helper methods
    # ----------------------------------------
    @classmethod
    def _split_path(cls,keyPath):
        hkey,path=keyPath.split('\\',1)
        if hkey not in cls.HKEY_CONSTANTS:
            raise Exception('HKEY not recognised: {}'.format(hkey))
        return cls.HKEY_CONSTANTS[hkey],path



    def __str__(self):
        return '{}\\{}'.format(self.HKEYS[self.hkey_constant],self.path)



# ----------------------------------------
# RegValue class
# ----------------------------------------
class RegValue(object):
    """Represents a value at a particular path in the registry."""

    def __init__(self,path,name):
        self.path=path
        self.name=name
        # why am I saving these things again? Because sub values?
        # self.reg_value=reg_value
        # self.reg_type=reg_type


    # ----------------------------------------
    # Types
    # ----------------------------------------
    class Type:
        def reg_value_type(self):
            raise NotImplemented

        def reg_value(self):
            raise NotImplemented

    class ExpandingString(str,Type):
        """ExpandingString is just a str but subclasses so instanceof can be used to differentiate"""
        def __new__(cls,value,*args,**kwargs):
            return  super(RegValue.ExpandingString,cls).__new__(cls,value)

        def reg_value_type(self):
            return winreg.REG_EXPAND_SZ

        def reg_value(self):
            return self

    class SignedInt(int,Type):
        """SignedInt is an int that can be converted to a DWORD type"""
        def __new__(cls,value,*args,**kwargs):
            # if value is an unsigned 32-bit value, convert to signed (we are probably reading from the registry)
            if value>2**31:
                value=value-2**32
            return  super(RegValue.SignedInt,cls).__new__(cls,value)

        def reg_value_type(self):
            return winreg.REG_DWORD

        def reg_value(self):
            """Convert to an unsigned DWORD value for setting in the registry"""
            if self<0:
                return 2**32+self
            return self


    def exists(self):
        """Tries to get this value to see if it exists."""
        try:
            self.get_raw()
            return True
        except OSError as e:
            if e.winerror==2: return False
            raise


    def get(self,type_class=None):
        """
        Returns the value or raises an exception if the key or value do not exist.
        If `type` is provided, will return `type(reg_value)` instead of just `reg_value`.
        Several built-in types are provided:
         - RegValue.ExpandingString() - a str; autodetected if the registry type is `REG_EXPAND_SZ`
         - RegValue.SignedInt() - an int; cannot be autodetected, but converts an unsigned REG_DWORD into a signed int
        """
        reg_value,reg_type=self.get_raw()
        if type_class:
            return type_class(reg_value)
        if reg_type==winreg.REG_EXPAND_SZ:
            return RegValue.ExpandingString(reg_value)
        return reg_value

    def get_raw(self):
        """
        Returns a tuple of `(reg_value,reg_type)` or raises an exception if the key or value do not exist.
        """
        handle=_open_key(self.path)
        try:
            reg_value,reg_type=winreg.QueryValueEx(handle,self.name)
        finally:
            handle.Close()
        return (reg_value,reg_type)


    def set(self,value):
        """
        Sets the value and creates the key if it doesn't exist.
        If value is not an instance of `RegValue.Type` then the reg_type is guessed by examining the type of `value` - see _guess_reg_type_from_value
        """
        handle=winreg.CreateKey(self.path.hkey_constant,self.path.path)
        if isinstance(value,RegValue.Type):
            reg_value=value.reg_value()
            reg_type=value.reg_value_type()
        else:
            (reg_value,reg_type)=self._guess_reg_type_from_value(value)

        try:
            winreg.SetValueEx(handle,self.name,0,reg_type,reg_value)
        finally:
            handle.Close()


    def delete(self):
        """Deletes a value. Just returns if it wasn't found or the key doesn't exist."""
        handle=_open_key(self.path,winreg.KEY_WRITE,error_on_non_existent=False)
        if not handle: return
        _ignore_file_not_found_error(lambda:winreg.DeleteValue(handle,self.name),finallyFn=lambda:handle.Close())


    @classmethod
    def _guess_reg_type_from_value(cls,value):
        """
        Determines what registry value type should be used based on the value:
         - str - REG_SZ
         - RegValue.ExpandingString - REG_EXPAND_SZ
         - path - REG_SZ
         - bytes - REG_BINARY
         - int - REG_DWORD

        Returns a tuple of `(reg_value,reg_type)`.
         - `reg_value` is a registry acceptable version of that value, eg. `Path` objects are converted into `str`s
         - `reg_type` is the winreg type, eg. winreg.REG_DWORD
        """
        if isinstance(value,bytes):
            return (value,winreg.REG_BINARY)
        if isinstance(value,RegValue.ExpandingString):
            return (value,winreg.REG_EXPAND_SZ)
        if isinstance(value,str):
            return (value,winreg.REG_SZ)
        if isinstance(value,Path):
            return (str(value),winreg.REG_SZ)
        if isinstance(value,int):
            return (value,winreg.REG_DWORD)
        raise Exception(f'Reg Type of "{value}" could not be determined')
