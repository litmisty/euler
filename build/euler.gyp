{
  'includes': ['common.gypi'],
  'target_defaults': {
    'msvs_settings': {
      'VCCLCompilerTool': {
        'WarningLevel': '4', # /W4
      },
    },
    'xcode_settings': {
      'GCC_VERSION': 'com.apple.compilers.llvm.clang.1_0',
      'CLANG_CXX_LANGUAGE_STANDARD': 'c++0x',
      'MACOSX_DEPLOYMENT_TARGET': '10.8', # OS X Deployment Target: 10.8
      'CLANG_CXX_LIBRARY': 'libc++', # libc++ requires OS X 10.7 or later
    },
	'conditions': [
      ['OS == "mac"', {
        'CXX': ['/usr/bin/clang++'],
        'LINK': ['/usr/bin/clang++'],
        'include_dirs': [
          '/usr/local/include',
        ],
      }], # OS == "mac"
      ['OS == "linux"', {
        'CXX': ['/usr/bin/g++'],
        'LINK': ['/usr/bin/g++'],
        'cflags': ['-std=c++0x'],
      }], # OS == "linux"
    ],
  },
  'targets': [
    {
      'target_name': 'q1',
      'product_name': 'q1',
      'type': 'executable',
      'include_dirs': [
        '../src/answers/q1',
      ],
      'sources': [
        '../src/answers/q1/main.cpp',
      ],
      'xcode_settings': {
      },
    },
    {
      'target_name': 'q2',
      'product_name': 'q2',
      'type': 'executable',
      'include_dirs': [
        '../src/answers/q2',
        '../src/utils',
      ],
      'sources': [
        '../src/answers/q2/main.cpp',
      ],
      'xcode_settings': {
      },
    },
    {
      'target_name': 'q3',
      'product_name': 'q3',
      'type': 'executable',
      'include_dirs': [
        '../src/answers/q3',
        '../src/utils',
      ],
      'sources': [
        '../src/answers/q3/main.cpp',
      ],
      'xcode_settings': {
      },
    },
  ] # targets
}
