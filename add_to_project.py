# https://gist.github.com/shurcooL/c99a5a32551906f8a147
import sublime
import sublime_plugin
import os.path

# Add folder that contains current file to sidebar.
class AddToProjectCommand(sublime_plugin.WindowCommand):
	def run(self):
		path = sublime.active_window().active_view().file_name()
		if path == None:
			return
		path = os.path.dirname(path)

		# TODO: Try to see if it's possible to preserve expanded folders when adding a new folder.
		#wat = sublime.active_window().active_view().settings().has("expanded_folders")
		#if wat:
		#	sublime.message_dialog("true")
		#else:
		#	sublime.message_dialog("false")

		data = sublime.active_window().project_data()
		if data:
			for folder in data['folders']:
				if folder['path'] == path:
					return
			data['folders'].append({'follow_symlinks': True, 'path': path})
		else:
			data = {'folders': [{'follow_symlinks': True, 'path': path}]}
		sublime.active_window().set_project_data(data)
