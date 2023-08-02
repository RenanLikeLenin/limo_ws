# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from summer_project/limo_info_array.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg
import summer_project.msg

class limo_info_array(genpy.Message):
  _md5sum = "0158dec9a13d04c5547357c0652c57cd"
  _type = "summer_project/limo_info_array"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """limo_info[] limo_infos

================================================================================
MSG: summer_project/limo_info
std_msgs/Int64 ID
std_msgs/Float64 mp_dist
std_msgs/Float64 origin_dist
std_msgs/Float64 vel
std_msgs/Float64 x
std_msgs/Float64 y
std_msgs/String path

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
  __slots__ = ['limo_infos']
  _slot_types = ['summer_project/limo_info[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       limo_infos

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(limo_info_array, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.limo_infos is None:
        self.limo_infos = []
    else:
      self.limo_infos = []

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
      length = len(self.limo_infos)
      buff.write(_struct_I.pack(length))
      for val1 in self.limo_infos:
        _v1 = val1.ID
        _x = _v1.data
        buff.write(_get_struct_q().pack(_x))
        _v2 = val1.mp_dist
        _x = _v2.data
        buff.write(_get_struct_d().pack(_x))
        _v3 = val1.origin_dist
        _x = _v3.data
        buff.write(_get_struct_d().pack(_x))
        _v4 = val1.vel
        _x = _v4.data
        buff.write(_get_struct_d().pack(_x))
        _v5 = val1.x
        _x = _v5.data
        buff.write(_get_struct_d().pack(_x))
        _v6 = val1.y
        _x = _v6.data
        buff.write(_get_struct_d().pack(_x))
        _v7 = val1.path
        _x = _v7.data
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
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
      if self.limo_infos is None:
        self.limo_infos = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.limo_infos = []
      for i in range(0, length):
        val1 = summer_project.msg.limo_info()
        _v8 = val1.ID
        start = end
        end += 8
        (_v8.data,) = _get_struct_q().unpack(str[start:end])
        _v9 = val1.mp_dist
        start = end
        end += 8
        (_v9.data,) = _get_struct_d().unpack(str[start:end])
        _v10 = val1.origin_dist
        start = end
        end += 8
        (_v10.data,) = _get_struct_d().unpack(str[start:end])
        _v11 = val1.vel
        start = end
        end += 8
        (_v11.data,) = _get_struct_d().unpack(str[start:end])
        _v12 = val1.x
        start = end
        end += 8
        (_v12.data,) = _get_struct_d().unpack(str[start:end])
        _v13 = val1.y
        start = end
        end += 8
        (_v13.data,) = _get_struct_d().unpack(str[start:end])
        _v14 = val1.path
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v14.data = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v14.data = str[start:end]
        self.limo_infos.append(val1)
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
      length = len(self.limo_infos)
      buff.write(_struct_I.pack(length))
      for val1 in self.limo_infos:
        _v15 = val1.ID
        _x = _v15.data
        buff.write(_get_struct_q().pack(_x))
        _v16 = val1.mp_dist
        _x = _v16.data
        buff.write(_get_struct_d().pack(_x))
        _v17 = val1.origin_dist
        _x = _v17.data
        buff.write(_get_struct_d().pack(_x))
        _v18 = val1.vel
        _x = _v18.data
        buff.write(_get_struct_d().pack(_x))
        _v19 = val1.x
        _x = _v19.data
        buff.write(_get_struct_d().pack(_x))
        _v20 = val1.y
        _x = _v20.data
        buff.write(_get_struct_d().pack(_x))
        _v21 = val1.path
        _x = _v21.data
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
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
      if self.limo_infos is None:
        self.limo_infos = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.limo_infos = []
      for i in range(0, length):
        val1 = summer_project.msg.limo_info()
        _v22 = val1.ID
        start = end
        end += 8
        (_v22.data,) = _get_struct_q().unpack(str[start:end])
        _v23 = val1.mp_dist
        start = end
        end += 8
        (_v23.data,) = _get_struct_d().unpack(str[start:end])
        _v24 = val1.origin_dist
        start = end
        end += 8
        (_v24.data,) = _get_struct_d().unpack(str[start:end])
        _v25 = val1.vel
        start = end
        end += 8
        (_v25.data,) = _get_struct_d().unpack(str[start:end])
        _v26 = val1.x
        start = end
        end += 8
        (_v26.data,) = _get_struct_d().unpack(str[start:end])
        _v27 = val1.y
        start = end
        end += 8
        (_v27.data,) = _get_struct_d().unpack(str[start:end])
        _v28 = val1.path
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v28.data = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v28.data = str[start:end]
        self.limo_infos.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_d = None
def _get_struct_d():
    global _struct_d
    if _struct_d is None:
        _struct_d = struct.Struct("<d")
    return _struct_d
_struct_q = None
def _get_struct_q():
    global _struct_q
    if _struct_q is None:
        _struct_q = struct.Struct("<q")
    return _struct_q
