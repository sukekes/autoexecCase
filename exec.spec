# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['testcase\\execcase\\exec_case.py',
              'common\\log.py',
              'common\\parse.py',
              'pages\\basepage.py',
              'pages\\exec_case.py',
              'pages\\loginpage.py',
              'pages\\personal_work.py',
              'testcase\\loginpage\\login_by_manager.py',
              'testcase\\personalwork\\personal_work.py'],
             pathex=['E:\\pws\\autoexecCase'],
             binaries=[('logs\\execute.log','.')],
             datas=[('testdata', 'testdata')],
             hiddenimports=['pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='exec_case',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='exec_case')
