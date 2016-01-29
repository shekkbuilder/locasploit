#!/usr/bin/env python
from _generic_plugin import *

# File should be named according to its name (it is not mandatory, but it is good for clarity). It must have a .py extension.

class Module(GenericModule):
	def __init__(self):
		self.authors = [
			# Define all authors of this module here. Email and Web is optional.
			Author(name='', email='', web=''),
		]
		
		# Name must be unique and should be in dot notation (e.g. linux.enumeration.distribution).
		# For clarity, the file name should be the same, with dots replaced by underscores (_) and .py extension. 
		# Do not use search symbols (brackets, ~, |, &)
		self.name = 'template'
		# Use this field as a SHORT description. This will be shown when modules are listed.
		self.short_description = 'Serves as a module template.'
		# Here you can specify links to books, blogs, whitepapers, CVEs etc.
		self.references = [
			'',
		]
		# Specify the date in exactly this format (yyyy-mm-dd). This can be used for searching or sorting.
		self.date = '2999-12-31'
		# You can define the license of the module here.
		self.license = 'GNU GPLv2'
		# If any change is made after the publishing, you must change the version.
		self.version = '0.0'
		# Tags are useful for searching. Do not use search keywords and symbols (and, not, or, &, |, !, brackets)
		self.tags = [
			'template',
		]
		# This is long description. You can (should) write anything important and useful here.  You should define what the module does, what files it access and whether it can do harm.
		self.description = """
This module is designed to be used as a template for new modules. 
Tired of the comments? Check the "template" module.
"""
		# If structures in knowledge base will be accessed, you should specify them here. Modules can be searched based on these fields. Do not use search keywords and symbols, number keys and spaces.
		self.kb_access = [
			#'USERS',
		]
		
		# If other modules are run directly from this module, you must specify the name and version. Dependencies will be checked for existence prior to execution.
		self.dependencies = {
			#'linux.enumeration.distribution': '1.0',
		}
		# If you like to redefine the modules frequently, consider to write some changelog.
		self.changelog = """
"""

		self.ResetParameters() # do not touch this

	def ResetParameters(self):
		# Define module parameters here. You should use UPPERCASE letters as a name. If value is not inialized and a global parameter with the same name exists, its value is used. Do not use spaces.
		# If the parameters is marked as kb or dependency, value is checked for existence (in kb or module list) before the execution.
		# For KB subkeys use dot notation (e.g. DISTRIBUTION.OS-RELEASE).
		# For dependencty, abbreviations can be used.
		# Always define SILENT parameter and do not print anything (except cricital errors) if SILENT==yes - for intermodule calls
		self.parameters = {
			'SILENT': Parameter(value='no', mandatory=True, description='Suppress the output', kb=False, dependency=False),
		}

	def Check(self):
		# If the module can be checked for success without execution (like some exploits), you should do it here. Do not use any dependencies.
		log.info('This module does not support check.')
	
	def Run(self):
		silent = positive(self.parameters['SILENT'].value)
		# # # # # # # #
		# Define your code here
		log.ok('Template module says: "Hello World!"')
		# # # # # # # #
		# If the module should terminate, return None. If it should run in the background, return the instance of the thread.
		return None	
	

lib.module_objects.append(Module())