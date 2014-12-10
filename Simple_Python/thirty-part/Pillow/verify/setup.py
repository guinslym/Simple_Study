setup(
	name='verifycode',
	version='0.1',
	package=['verify'],
	author='yafeile',
	author_email='zhuzhulang@126.com',
	license='LGPL',
	description='A verify code in python',
	keywords='code verify',
	install_requires=["Pillow>=2.0"],
	entry_point={
	'console_scripts':[
	 'verifycode=VerifyCode.VerifyCode:main'
	]
	}
)