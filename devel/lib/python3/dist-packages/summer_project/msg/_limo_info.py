# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from summer_project/limo_info.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class limo_info(genpy.Message):
  _md5sum = "24e962fd472c2ad4988156ac52134873"
  _type = "summer_project/limo_info"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """std_msgs/Int64 ID
std_msgs/Float64 vel
std_msgs/Float64 x
std_msgs/Float64 y
std_msgs/Float64 mp_dist
std_msgs/Float64 origin_dist
std_msgs/String path

std_msgs/Float64 d1
std_msgs/Float64 d2

================================================================================
MSG: std_msgs/Int64
int64 data
================================================================================
MSG: std_msgs/Float64
float64 data
================================================================================
MSG: std_msgs/String
string data
"""
  __slots__ = ['ID','vel','x','y','mp_dist','origin_dist','path','d1','d2']
  _slot_types = ['std_msgs/Int64','std_msgs/Float64','std_msgs/Float64','std_msgs/Float64','std_msgs/Float64','std_msgs/Float64','std_msgs/String','std_msgs/Float64','std_msgs/Float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ID,vel,x,y,mp_dist,origin_dist,path,d1,d2

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(limo_info, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.ID is None:
        self.ID = std_msgs.msg.Int64()
      if self.vel is None:
        self.vel = std_msgs.msg.Float64()
      if self.x is None:
        self.x = std_msgs.msg.Float64()
      if self.y is None:
        self.y = std_msgs.msg.Float64()
      if self.mp_dist is None:
        self.mp_dist = std_msgs.msg.Float64()
      if self.origin_dist is None:
        self.origin_dist = std_msgs.msg.Float64()
      if self.path is None:
        self.path = std_msgs.msg.String()
      if self.d1 is None:
        self.d1 = std_msgs.msg.Float64()
      if self.d2 is None:
        self.d2 = std_msgs.msg.Float64()
    else:
      self.ID = std_msgs.msg.Int64()
      self.vel = std_msgs.msg.Float64()
      self.x = std_msgs.msg.Float64()
      self.y = std_msgs.msg.Float64()
      self.mp_dist = std_msgs.msg.Float64()
      self.origin_dist = std_msgs.msg.Float64()
      self.path = std_msgs.msg.String()
      self.d1 = std_msgs.msg.Float64()
      self.d2 = std_msgs.msg.Float64()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_q5d().pack(_x.ID.data, _x.vel.data, _x.x.data, _x.y.data, _x.mp_dist.data, _x.origin_dist.data))
      _x = self.path.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2d().pack(_x.d1.data, _x.d2.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.ID is None:
        self.ID = std_msgs.msg.Int64()
      if self.vel is None:
        self.vel = std_msgs.msg.Float64()
      if self.x is None:
        self.x = std_msgs.msg.Float64()
      if self.y is None:
        self.y = std_msgs.msg.Float64()
      if self.mp_dist is None:
        self.mp_dist = std_msgs.msg.Float64()
      if self.origin_dist is None:
        self.origin_dist = std_msgs.msg.Float64()
      if self.path is None:
        self.path = std_msgs.msg.String()
      if self.d1 is None:
        self.d1 = std_msgs.msg.Float64()
      if self.d2 is None:
        self.d2 = std_msgs.msg.Float64()
      end = 0
      _x = self
      start = end
      end += 48
      (_x.ID.data, _x.vel.data, _x.x.data, _x.y.data, _x.mp_dist.data, _x.origin_dist.data,) = _get_struct_q5d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.path.data = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.path.data = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.d1.data, _x.d2.data,) = _get_struct_2d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_q5d().pack(_x.ID.data, _x.vel.data, _x.x.data, _x.y.data, _x.mp_dist.data, _x.origin_dist.data))
      _x = self.path.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2d().pack(_x.d1.data, _x.d2.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.ID is None:
        self.ID = std_msgs.msg.Int64()
      if self.vel is None:
        self.vel = std_msgs.msg.Float64()
      if self.x is None:
        self.x = std_msgs.msg.Float64()
      if self.y is None:
        self.y = std_msgs.msg.Float64()
      if self.mp_dist is None:
        self.mp_dist = std_msgs.msg.Float64()
      if self.origin_dist is None:
        self.origin_dist = std_msgs.msg.Float64()
      if self.path is None:
        self.path = std_msgs.msg.String()
      if self.d1 is None:
        self.d1 = std_msgs.msg.Float64()
      if self.d2 is None:
        self.d2 = std_msgs.msg.Float64()
      end = 0
      _x = self
      start = end
      end += 48
      (_x.ID.data, _x.vel.data, _x.x.data, _x.y.data, _x.mp_dist.data, _x.origin_dist.data,) = _get_struct_q5d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.path.data = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.path.data = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.d1.data, _x.d2.data,) = _get_struct_2d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2d = None
def _get_struct_2d():
    global _struct_2d
    if _struct_2d is None:
        _struct_2d = struct.Struct("<2d")
    return _struct_2d
_struct_q5d = None
def _get_struct_q5d():
    global _struct_q5d
    if _struct_q5d is None:
        _struct_q5d = struct.Struct("<q5d")
    return _struct_q5d
