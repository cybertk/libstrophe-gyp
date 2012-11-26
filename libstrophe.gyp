# Copyright (c) 2012 cybertk.com. All rights reserved.
{
  'variables': {
    # Available values are 'none', 'openssl', 'gnutls'.
    'strophe_tls%': 'none',
    # Available values are 'libxml', 'expat'.
    'strophe_xml%': 'libxml',

    'use_system_libxml%': 0,
    'use_system_expat': 0,
    'use_system_openssl%': 0,
    'use_system_gnutls': 0,

    'conditions': [
      # Use expat as xml backend on Android, as expat is lightweight.
      ['OS == "android"', {
        'strophe_xml': 'expat',
      }],
    ],
  },

  'targets': [
    {
      'target_name': 'strophe',
      'type': '<(library)',

      'conditions': [

        # libxml backend compiling configuration.
        ['strophe_xml == "libxml"', {
          'sources': [
            'src/parser_libxml2.c',
          ],

          'conditions': [
            ['use_system_libxml', {

              'include_dirs': [
                '/usr/include/libxml2/',
              ],
              'link_settings': {
                'libraries': [
                  '-lxml2',
                ],
              },
            }, { # !use_system_libxml
              'dependencies': [
                '<(DEPTH)/third_party/libxml/libxml.gyp:libxml',
              ],
            }],
          ],
        }], # strophe_xml == "libxml"

        # expat backend compiling configuration.
        ['strophe_xml == "expat"', {
          'sources': [
            'src/parser_expat.c',
          ],

          'conditions': [
            ['use_system_expat', {
              'link_settings': {
                'libraries': [
                  '-lexpat',
                ],
              },
            }, { # !use_system_expat
              'dependencies': [
                '<(DEPTH)/third_party/openssl/openssl.gyp:openssl',
              ],
            }],
          ],
        }], # strophe_xml == "expat"


        # openssl backend compiling configuration.
        ['strophe_tls == "none"', {
          'sources': [
            'src/tls_dummy.c',
          ],
        }], # strophe_tls == "none"

        # openssl backend compiling configuration.
        ['strophe_tls == "openssl"', {
          'sources': [
            'src/tls_openssl.c',
          ],

          'conditions': [
            ['use_system_openssl', {
              'link_settings': {
                'libraries': [
                  '-lssl',
                ],
              },
            }, { # !use_system_openssl
              'dependencies': [
                '<(DEPTH)/third_party/openssl/openssl.gyp:openssl',
              ],
            }],
          ],
        }], # strophe_tls == "openssl"

        # openssl backend compiling configuration.
        ['strophe_tls == "gnutls"', {
          'sources': [
            'src/tls_gnutls.c',
          ],

          'conditions': [
            ['use_system_guntls', {
              'link_settings': {
                'libraries': [
                  '-lgnutls',
                ],
              },
            }, { # !use_system_gnutls
              'dependencies': [
                '<(DEPTH)/third_party/gnutls/gnutls.gyp:gnutls',
              ],
            }],
          ],
        }], # strophe_tls == "gnutls"
      ], # conditions.

      'sources': [
          'src/auth.c',
          'src/conn.c',
          'src/ctx.c',
          'src/event.c',
          'src/handler.c',
          'src/hash.c',
          'src/jid.c',
          'src/md5.c',
          'src/oocontext.cpp',
          'src/oostanza.cpp',
          'src/sasl.c',
          'src/sha1.c',
          'src/snprintf.c',
          'src/sock.c',
          'src/stanza.c',
          'src/thread.c',
          #'src/tls_schannel.c',
          'src/util.c',
      ],

      'include_dirs': [
          '.',
          'src/',
      ],

      'direct_dependent_settings': {
        'include_dirs': [
          '.',
          'src',
        ],
      },
    }
  ], # targets
}
