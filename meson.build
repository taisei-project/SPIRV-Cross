project('SPIRV-Cross', 'cpp',
    license : 'Apache-2.0',
    version : run_command(files('get_version.py')).stdout().strip(),
    meson_version : '>=0.48.0',
    default_options : [
        'cpp_std=c++11',
    ]
)

add_project_arguments(
    meson.get_compiler('cpp').get_supported_arguments(
        '-fno-exceptions',
        '-fno-rtti',
    ),
    language : 'cpp',
)

spvc_install = not meson.is_subproject()

spvc_defs = [
    '-DSPIRV_CROSS_C_API_CPP=1',
    '-DSPIRV_CROSS_C_API_GLSL=1',
    '-DSPIRV_CROSS_C_API_HLSL=1',
    '-DSPIRV_CROSS_C_API_MSL=1',
    '-DSPIRV_CROSS_C_API_REFLECT=1',
    '-DSPIRV_CROSS_EXCEPTIONS_TO_ASSERTIONS',
]

spvc_src = files(
    'spirv_cfg.cpp',
    'spirv_cpp.cpp',
    'spirv_cross.cpp',
    'spirv_cross_c.cpp',
    'spirv_cross_parsed_ir.cpp',
    'spirv_cross_util.cpp',
    'spirv_glsl.cpp',
    'spirv_hlsl.cpp',
    'spirv_msl.cpp',
    'spirv_parser.cpp',
    'spirv_reflect.cpp',
)

spvc_hdr = files(
    'GLSL.std.450.h',
    'spirv_cfg.hpp',
    'spirv_common.hpp',
    'spirv_cpp.hpp',
    'spirv_cross_c.h',
    'spirv_cross.hpp',
    'spirv_cross_parsed_ir.hpp',
    'spirv_cross_util.hpp',
    'spirv_glsl.hpp',
    'spirv.h',
    'spirv_hlsl.hpp',
    'spirv.hpp',
    'spirv_msl.hpp',
    'spirv_parser.hpp',
    'spirv_reflect.hpp',
)

spvc_incdirs = include_directories('.', 'include')

libspirv_cross = library('spirv-cross',
    spvc_src,
    cpp_args : spvc_defs,
    build_by_default : not meson.is_subproject(),
    include_directories : spvc_incdirs,
    gnu_symbol_visibility : 'hidden',
    install : spvc_install,
)

spirv_cross_dep = declare_dependency(
    link_with : libspirv_cross,
    include_directories : spvc_incdirs,
)

if spvc_install
    install_headers(spvc_hdr, subdir : 'spirv_cross')

    pkg = import('pkgconfig')
    pkg.generate(libspirv_cross,
        subdirs : 'spirv_cross',
        version : '0.13.0'
    )
endif
