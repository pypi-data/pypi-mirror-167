import ctypes

memhole = ctypes.cdll.LoadLibrary("./memhole.so")
memhole.create_memhole.restype = ctypes.c_void_p
memhole.delete_memhole.argtypes = [ctypes.c_void_p]
memhole.attach_to_pid.argtypes = [ctypes.c_void_p, ctypes.c_int]
memhole.attach_to_pid.restype = ctypes.c_long
memhole.set_buffer_size.argtypes = [ctypes.c_void_p, ctypes.c_int]
memhole.set_buffer_size.restype = ctypes.c_int
memhole.get_memory_position.argtypes = [ctypes.c_void_p]
memhole.get_memory_position.restype = ctypes.c_void_p
memhole.set_memory_position.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
memhole.set_memory_position.restype = ctypes.c_void_p
memhole.read_memory.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_long, ctypes.c_int]
memhole.read_memory.restype = ctypes.c_long
memhole.connect_memhole.argtypes = [ctypes.c_void_p]
memhole.buffer_creator.argtypes = [ctypes.c_void_p, ctypes.c_long]
memhole.buffer_creator.restype = ctypes.c_char_p
memhole.printf_wrapper.argtypes = [ctypes.c_char_p, ctypes.c_long]
memhole.disconnect_memhole.argtypes = [ctypes.c_void_p]
memhole.disconnect_memhole.restype = ctypes.c_int
memhole.buffer_deleter.argtypes = [ctypes.c_void_p]