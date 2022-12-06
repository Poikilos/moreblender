#!/usr/bin/env python3
"""
This takes a blend file argument and prints out some of its details, eg:

  blend_info.py /path/to/test.blend
"""
# Must run with the blender python such as:
# C:\Program Files\Blender Foundation\Blender 3.3\3.3\python\bin
import os


import sys
PROGRAM_FILES = os.path.join("C:\\", "Program Files")
# ^ Add \\ otherwise join won't add it :(
version_dir = os.path.join(PROGRAM_FILES, "Blender Foundation",
						   "Blender 3.3", "3.3")
blender_env = os.path.join(version_dir, "python", "lib")
modules = os.path.join(version_dir, "scripts", "modules")
# C:\Program Files\Blender Foundation\Blender 3.3\3.3\scripts\modules

sys.path.insert(0, blender_env)
sys.path.insert(0, modules)

blend_render_info_path = os.path.join(modules, "blend_render_info.py")
if not os.path.isfile(blend_render_info_path):
	raise FileNotFoundError(blend_render_info_path)

def main():
	'''
	# See second example at <https://blender.stackexchange.com/a/55503>
	import blendfile  # Deprecated 

	filepath = sys.argv[-1]
	with blendfile.open_blend(filepath) as blend:
		scenes = [b for b in blend.blocks if b.code == b'SC']
		for scene in scenes:
			name =          scene[b'id', b'name'][2:].decode('utf-8')
			path =          scene[b'r', b'pic'].decode('utf-8')
			frame_start =   scene[b'r', b'sfra']
			frame_end =     scene[b'r', b'efra']

			print(frame_start, frame_end, repr(name), repr(path))

	^ 
	`blendfile.py` was removed (as unsupported) in 2019 - see commit 
	[developer.blender.org/rBACbdf03453e8a0]
	(https://developer.blender.org/rBACbdf03453e8a0) 
	and ticket 
	[developer.blender.org/T63750](https://developer.blender.org/T63750) 
	but `blend_render_info.py` still works - for the 3.1.x series you'll 
	find it under `3.1/scripts/modules` in your root Blender directory. 
	\\endgroup

	– [George 
	Hawkins](https://blender.stackexchange.com/users/124535/george-hawkins 
	"311 reputation")

	[Jun 6 at  19:32](https://blender.stackexchange.com/questions/55499/
	how-to-extract-render-info-from-a-blend-file-without-launching-blender
	#comment453867_55503)
	'''

	# See <https://blender.stackexchange.com/a/55503>:
	# blend_render_info.py is in modules.
	# import bpy  # only works in Blender, since imports _bpy (Blender C module)
	# filepath = bpy.data.filepath  # test within Blender
	filepath = sys.argv[1]

	# print("This doesn't show much.")

	import blend_render_info
	data = blend_render_info.read_blend_rend_chunk(filepath)
	for frame_start, frame_end, scene_name in data:
		print(frame_start, frame_end, scene_name)
	return 0

if __name__ == "__main__":
	sys.exit(main())
