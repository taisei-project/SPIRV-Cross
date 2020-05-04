project('SPIRV-Cross', 'cpp',
    license : 'Apache-2.0',
    version : run_command(files('get_version.py')).stdout().strip(),
    meson_version : '>=0.48.0',
    default_options : [
        'cpp_std=gnu++11',
    ]
)

native_options = [
    'b_lto=false',
    'b_ndebug=true',
    'b_sanitize=none',
    'debug=false',
    'optimization=0',
]

add_project_arguments(
    meson.get_compiler('cpp').get_supported_arguments(
        '-fno-exceptions',
        '-fno-rtti',
    ),
    language : 'cpp',
)

add_project_arguments(
    meson.get_compiler('cpp', native : true).get_supported_arguments(
        '-fno-exceptions',
        '-fno-rtti',
    ),
    language : 'cpp',
    native : true,
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
    version : meson.project_version(),
)

libspirv_cross_native = static_library('spirv-cross-native',
    spvc_src,
    cpp_args : spvc_defs,
    build_by_default : false,
    include_directories : spvc_incdirs,
    gnu_symbol_visibility : 'hidden',
    install : false,
    native : true,
    override_options : native_options,
)

spirv_cross_native_dep = declare_dependency(
    link_with : libspirv_cross_native,
    include_directories : spvc_incdirs,
    version : meson.project_version(),
)

spirv_cross_native = executable('spirv-cross',
    'main.cpp',
    cpp_args : spvc_defs,
    dependencies : spirv_cross_native_dep,
    native : true,
    build_by_default : false,
    override_options : native_options,
)

if spvc_install
    install_headers(spvc_hdr, subdir : 'spirv_cross')

    pkg = import('pkgconfig')
    pkg.generate(libspirv_cross,
        subdirs : 'spirv_cross',
        version : meson.project_version()
    )
endif
