# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from summer_project/limo_info.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class limo_info(genpy.Message):
  _md5sum = "326e2462ad523a29cf0e1a6ca744aac8"
  _type = "summer_project/limo_info"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """std_msgs/Int64 ID
std_msgs/Float64 x
std_msgs/Float64 y
std_msgs/Float64 vel
std_msgs/Float64 acc

================================================================================
MSG: std_msgs/Int64
int64 data
================================================================================
MSG: std_msgs/Float64
float64 data"""
  __slots__ = ['ID','x','y','vel','acc']
  _slot_types = ['std_msgs/Int64','std_msgs/Float64','std_msgs/Float64','std_msgs/Float64','std_msgs/Float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ID,x,y,vel,acc

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(limo_info, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.ID is None:
        self.ID = std_msgs.msg.Int64()
      if self.x is None:
        self.x = std_msgs.msg.Float64()
      if self.y is None:
        self.y = std_msgs.msg.Float64()
      if self.vel is None:
        self.vel = std_msgs.msg.Float64()
      if self.acc is None:
        self.acc = std_msgs.msg.Float64()
    else:
      self.ID = std_msgs.msg.Int64()
      self.x = std_msgs.msg.Float64()
      self.y = std_msgs.msg.Float64()
      self.vel = std_msgs.msg.Float64()
      self.acc = std_msgs.msg.Float64()

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
      buff.write(_get_struct_q4d().pack(_x.ID.data, _x.x.data, _x.y.data, _x.vel.data, _x.acc.data))
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
      if self.x is None:
        self.x = std_msgs.msg.Float64()
      if self.y is None:
        self.y = std_msgs.msg.Float64()
      if self.vel is None:
        self.vel = std_msgs.msg.Float64()
      if self.acc is None:
        self.acc = std_msgs.msg.Float64()
      end = 0
      _x = self
      start = end
      end += 40
      (_x.ID.data, _x.x.data, _x.y.data, _x.vel.data, _x.acc.data,) = _get_struct_q4d().unpack(str[start:end])
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
      buff.write(_get_struct_q4d().pack(_x.ID.data, _x.x.data, _x.y.data, _x.vel.data, _x.acc.data))
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
      if self.x is None:
        self.x = std_msgs.msg.Float64()
      if self.y is None:
        self.y = std_msgs.msg.Float64()
      if self.vel is None:
        self.vel = std_msgs.msg.Float64()
      if self.acc is None:
        self.acc = std_msgs.msg.Float64()
      end = 0
      _x = self
      start = end
      end += 40
      (_x.ID.data, _x.x.data, _x.y.data, _x.vel.data, _x.acc.data,) = _get_struct_q4d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_q4d = None
def _get_struct_q4d():
    global _struct_q4d
    if _struct_q4d is None:
        _struct_q4d = struct.Struct("<q4d")
    return _struct_q4d
