[toc]

# SophomoreSummerTraining

暑假实训——CQU电影票房数据可视化

## CQU大数据与软件学院的暑假实训

（flask框架）

代码很冗长

具体见实训交付物文件夹

## 运行环境

pycharm

## 文件结构

```
│  README.md
│  
├─flask_showinfo
│  │  app.py
│  │  debug__.py
│  │  movie.db
│  │  movieCompany.db
│  │  movieTop2016_2022.db
│  │  temp
│  │  useful
│  │  
│  ├─.idea
│  │  │  .gitignore
│  │  │  dbnavigator.xml
│  │  │  flask_showinfo.iml
│  │  │  misc.xml
│  │  │  modules.xml
│  │  │  workspace.xml
│  │  │  
│  │  └─inspectionProfiles
│  │          profiles_settings.xml
│  │          
│  ├─static
│  │  │  About.css
│  │  │  About.html
│  │  │  bgm.mp3
│  │  │  Blog-Template.css
│  │  │  Blog-Template.html
│  │  │  Contact.css
│  │  │  Contact.html
│  │  │  echarts.min.js
│  │  │  Home.css
│  │  │  Home.html
│  │  │  jquery.js
│  │  │  nicepage.css
│  │  │  nicepage.js
│  │  │  Post-Template.css
│  │  │  Post-Template.html
│  │  │  
│  │  └─images
│  │          1.jpeg
│  │          1498833780.jpg
│  │          1498872925.jpg
│  │          1498990979.jpg
│  │          1499078541.jpg
│  │          1499126137.jpg
│  │          1499145314.jpg
│  │          1499171933.jpg
│  │          1499189752.jpg
│  │          1499256478.jpg
│  │          1499282435.jpg
│  │          1499354872.jpg
│  │          1656691638_221897.png
│  │          2.jpeg
│  │          20220703160101.jpg
│  │          20220703181851.jpg
│  │          20220703181911.jpg
│  │          3.jpeg
│  │          32BD0ED507CD534EC9E776B724EBE6FF.jpg
│  │          back.jpg
│  │          bakery-baking-berry-breakfast-213780.jpg
│  │          black-and-silver-coffee-maker-on-white-wooden-kitchen-4816319.jpg
│  │          breakfast-meals-on-table-803897.jpg
│  │          close-up-photo-of-sliced-chocolate-cake-4110008.jpg
│  │          default-image.jpg
│  │          ed-min.jpg
│  │          OIP-C (2).jpg
│  │          OIP-C (3).jpg
│  │          OIP-C (4).jpg
│  │          pexels-marta-dzedyshko-2067396.jpg
│  │          pexels-photo-3218467.jpeg
│  │          pexels-photo-4099237.jpeg
│  │          pexels-photo-4193838.jpeg
│  │          pexels-photo-5591663.jpeg
│  │          pexels-photo-5591712.jpeg
│  │          pexels-photo-5702782.jpeg
│  │          pexels-photo-5702789.jpeg
│  │          pexels-photo-5702791.jpeg
│  │          pexels-photo-949069.jpeg
│  │          photo1.webp
│  │          R-C.jpg
│  │          white-and-brown-cake-on-white-ceramic-plate-4110001.jpg
│  │          word.jpg
│  │          
│  └─templates
│          debug_test.py
│          home_page.html
│          testEcharts.html
│          
├─maoyan_info
│  │  debug.py
│  │  maoyan_info.py
│  │  resource
│  │  temp.woff
│  │  tempt.html
│  │  test.py
│  │  
│  └─.idea
│      │  .gitignore
│      │  dbnavigator.xml
│      │  maoyan_info.iml
│      │  misc.xml
│      │  modules.xml
│      │  workspace.xml
│      │  
│      └─inspectionProfiles
│              profiles_settings.xml
│              
├─实训交付物
│  │  20205644-李易燔-第一周周报.doc
│  │  20205644-李易燔-第二周周报.doc
│  │  李易燔——20205644——软件综合实践报告.doc
│  │  软件综合实践第三周总结-李易燔-20205644.doc
│  │  
│  └─交付物
│          软件综合实践报告模板.doc
│          软件综合实践第三周总结-报告-1班-20190000-张三-.doc
│          
└─电影票房数据可视化系统——20205644
    │  电影票房数据可视化系统.pdf
    │  
    ├─.idea
    │  │  .gitignore
    │  │  dbnavigator.xml
    │  │  misc.xml
    │  │  modules.xml
    │  │  workspace.xml
    │  │  电影票房数据可视化系统——20205644.iml
    │  │  
    │  └─inspectionProfiles
    │          profiles_settings.xml
    │          
    ├─venv
    │  │  .gitignore
    │  │  pyvenv.cfg
    │  │  
    │  ├─Lib
    │  │  └─site-packages
    │  │      │  distutils-precedence.pth
    │  │      │  pip-21.1.2.virtualenv
    │  │      │  setuptools-57.0.0.virtualenv
    │  │      │  wheel-0.36.2.virtualenv
    │  │      │  _virtualenv.pth
    │  │      │  _virtualenv.py
    │  │      │  
    │  │      ├─pip
    │  │      │  │  py.typed
    │  │      │  │  __init__.py
    │  │      │  │  __main__.py
    │  │      │  │  
    │  │      │  ├─_internal
    │  │      │  │  │  build_env.py
    │  │      │  │  │  cache.py
    │  │      │  │  │  configuration.py
    │  │      │  │  │  exceptions.py
    │  │      │  │  │  main.py
    │  │      │  │  │  pyproject.py
    │  │      │  │  │  self_outdated_check.py
    │  │      │  │  │  wheel_builder.py
    │  │      │  │  │  __init__.py
    │  │      │  │  │  
    │  │      │  │  ├─cli
    │  │      │  │  │      autocompletion.py
    │  │      │  │  │      base_command.py
    │  │      │  │  │      cmdoptions.py
    │  │      │  │  │      command_context.py
    │  │      │  │  │      main.py
    │  │      │  │  │      main_parser.py
    │  │      │  │  │      parser.py
    │  │      │  │  │      progress_bars.py
    │  │      │  │  │      req_command.py
    │  │      │  │  │      spinners.py
    │  │      │  │  │      status_codes.py
    │  │      │  │  │      __init__.py
    │  │      │  │  │      
    │  │      │  │  ├─commands
    │  │      │  │  │      cache.py
    │  │      │  │  │      check.py
    │  │      │  │  │      completion.py
    │  │      │  │  │      configuration.py
    │  │      │  │  │      debug.py
    │  │      │  │  │      download.py
    │  │      │  │  │      freeze.py
    │  │      │  │  │      hash.py
    │  │      │  │  │      help.py
    │  │      │  │  │      install.py
    │  │      │  │  │      list.py
    │  │      │  │  │      search.py
    │  │      │  │  │      show.py
    │  │      │  │  │      uninstall.py
    │  │      │  │  │      wheel.py
    │  │      │  │  │      __init__.py
    │  │      │  │  │      
    │  │      │  │  ├─distributions
    │  │      │  │  │      base.py
    │  │      │  │  │      installed.py
    │  │      │  │  │      sdist.py
    │  │      │  │  │      wheel.py
    │  │      │  │  │      __init__.py
    │  │      │  │  │      
    │  │      │  │  ├─index
    │  │      │  │  │      collector.py
    │  │      │  │  │      package_finder.py
    │  │      │  │  │      sources.py
    │  │      │  │  │      __init__.py
    │  │      │  │  │      
    │  │      │  │  ├─locations
    │  │      │  │  │      base.py
    │  │      │  │  │      _distutils.py
    │  │      │  │  │      _sysconfig.py
    │  │      │  │  │      __init__.py
    │  │      │  │  │      
    │  │      │  │  ├─metadata
    │  │      │  │  │      base.py
    │  │      │  │  │      pkg_resources.py
    │  │      │  │  │      __init__.py
    │  │      │  │  │      
    │  │      │  │  ├─models
    │  │      │  │  │      candidate.py
    │  │      │  │  │      direct_url.py
    │  │      │  │  │      format_control.py
    │  │      │  │  │      index.py
    │  │      │  │  │      link.py
    │  │      │  │  │      scheme.py
    │  │      │  │  │      search_scope.py
    │  │      │  │  │      selection_prefs.py
    │  │      │  │  │      target_python.py
    │  │      │  │  │      wheel.py
    │  │      │  │  │      __init__.py
    │  │      │  │  │      
    │  │      │  │  ├─network
    │  │      │  │  │      auth.py
    │  │      │  │  │      cache.py
    │  │      │  │  │      download.py
    │  │      │  │  │      lazy_wheel.py
    │  │      │  │  │      session.py
    │  │      │  │  │      utils.py
    │  │      │  │  │      xmlrpc.py
    │  │      │  │  │      __init__.py
    │  │      │  │  │      
    │  │      │  │  ├─operations
    │  │      │  │  │  │  check.py
    │  │      │  │  │  │  freeze.py
    │  │      │  │  │  │  prepare.py
    │  │      │  │  │  │  __init__.py
    │  │      │  │  │  │  
    │  │      │  │  │  ├─build
    │  │      │  │  │  │      metadata.py
    │  │      │  │  │  │      metadata_legacy.py
    │  │      │  │  │  │      wheel.py
    │  │      │  │  │  │      wheel_legacy.py
    │  │      │  │  │  │      __init__.py
    │  │      │  │  │  │      
    │  │      │  │  │  └─install
    │  │      │  │  │          editable_legacy.py
    │  │      │  │  │          legacy.py
    │  │      │  │  │          wheel.py
    │  │      │  │  │          __init__.py
    │  │      │  │  │          
    │  │      │  │  ├─req
    │  │      │  │  │      constructors.py
    │  │      │  │  │      req_file.py
    │  │      │  │  │      req_install.py
    │  │      │  │  │      req_set.py
    │  │      │  │  │      req_tracker.py
    │  │      │  │  │      req_uninstall.py
    │  │      │  │  │      __init__.py
    │  │      │  │  │      
    │  │      │  │  ├─resolution
    │  │      │  │  │  │  base.py
    │  │      │  │  │  │  __init__.py
    │  │      │  │  │  │  
    │  │      │  │  │  ├─legacy
    │  │      │  │  │  │      resolver.py
    │  │      │  │  │  │      __init__.py
    │  │      │  │  │  │      
    │  │      │  │  │  └─resolvelib
    │  │      │  │  │          base.py
    │  │      │  │  │          candidates.py
    │  │      │  │  │          factory.py
    │  │      │  │  │          found_candidates.py
    │  │      │  │  │          provider.py
    │  │      │  │  │          reporter.py
    │  │      │  │  │          requirements.py
    │  │      │  │  │          resolver.py
    │  │      │  │  │          __init__.py
    │  │      │  │  │          
    │  │      │  │  ├─utils
    │  │      │  │  │      appdirs.py
    │  │      │  │  │      compat.py
    │  │      │  │  │      compatibility_tags.py
    │  │      │  │  │      datetime.py
    │  │      │  │  │      deprecation.py
    │  │      │  │  │      direct_url_helpers.py
    │  │      │  │  │      distutils_args.py
    │  │      │  │  │      encoding.py
    │  │      │  │  │      entrypoints.py
    │  │      │  │  │      filesystem.py
    │  │      │  │  │      filetypes.py
    │  │      │  │  │      glibc.py
    │  │      │  │  │      hashes.py
    │  │      │  │  │      inject_securetransport.py
    │  │      │  │  │      logging.py
    │  │      │  │  │      misc.py
    │  │      │  │  │      models.py
    │  │      │  │  │      packaging.py
    │  │      │  │  │      parallel.py
    │  │      │  │  │      pkg_resources.py
    │  │      │  │  │      setuptools_build.py
    │  │      │  │  │      subprocess.py
    │  │      │  │  │      temp_dir.py
    │  │      │  │  │      unpacking.py
    │  │      │  │  │      urls.py
    │  │      │  │  │      virtualenv.py
    │  │      │  │  │      wheel.py
    │  │      │  │  │      __init__.py
    │  │      │  │  │      
    │  │      │  │  └─vcs
    │  │      │  │          bazaar.py
    │  │      │  │          git.py
    │  │      │  │          mercurial.py
    │  │      │  │          subversion.py
    │  │      │  │          versioncontrol.py
    │  │      │  │          __init__.py
    │  │      │  │          
    │  │      │  └─_vendor
    │  │      │      │  appdirs.py
    │  │      │      │  distro.py
    │  │      │      │  pyparsing.py
    │  │      │      │  six.py
    │  │      │      │  vendor.txt
    │  │      │      │  __init__.py
    │  │      │      │  
    │  │      │      ├─cachecontrol
    │  │      │      │  │  adapter.py
    │  │      │      │  │  cache.py
    │  │      │      │  │  compat.py
    │  │      │      │  │  controller.py
    │  │      │      │  │  filewrapper.py
    │  │      │      │  │  heuristics.py
    │  │      │      │  │  serialize.py
    │  │      │      │  │  wrapper.py
    │  │      │      │  │  _cmd.py
    │  │      │      │  │  __init__.py
    │  │      │      │  │  
    │  │      │      │  └─caches
    │  │      │      │          file_cache.py
    │  │      │      │          redis_cache.py
    │  │      │      │          __init__.py
    │  │      │      │          
    │  │      │      ├─certifi
    │  │      │      │      cacert.pem
    │  │      │      │      core.py
    │  │      │      │      __init__.py
    │  │      │      │      __main__.py
    │  │      │      │      
    │  │      │      ├─chardet
    │  │      │      │  │  big5freq.py
    │  │      │      │  │  big5prober.py
    │  │      │      │  │  chardistribution.py
    │  │      │      │  │  charsetgroupprober.py
    │  │      │      │  │  charsetprober.py
    │  │      │      │  │  codingstatemachine.py
    │  │      │      │  │  compat.py
    │  │      │      │  │  cp949prober.py
    │  │      │      │  │  enums.py
    │  │      │      │  │  escprober.py
    │  │      │      │  │  escsm.py
    │  │      │      │  │  eucjpprober.py
    │  │      │      │  │  euckrfreq.py
    │  │      │      │  │  euckrprober.py
    │  │      │      │  │  euctwfreq.py
    │  │      │      │  │  euctwprober.py
    │  │      │      │  │  gb2312freq.py
    │  │      │      │  │  gb2312prober.py
    │  │      │      │  │  hebrewprober.py
    │  │      │      │  │  jisfreq.py
    │  │      │      │  │  jpcntx.py
    │  │      │      │  │  langbulgarianmodel.py
    │  │      │      │  │  langgreekmodel.py
    │  │      │      │  │  langhebrewmodel.py
    │  │      │      │  │  langhungarianmodel.py
    │  │      │      │  │  langrussianmodel.py
    │  │      │      │  │  langthaimodel.py
    │  │      │      │  │  langturkishmodel.py
    │  │      │      │  │  latin1prober.py
    │  │      │      │  │  mbcharsetprober.py
    │  │      │      │  │  mbcsgroupprober.py
    │  │      │      │  │  mbcssm.py
    │  │      │      │  │  sbcharsetprober.py
    │  │      │      │  │  sbcsgroupprober.py
    │  │      │      │  │  sjisprober.py
    │  │      │      │  │  universaldetector.py
    │  │      │      │  │  utf8prober.py
    │  │      │      │  │  version.py
    │  │      │      │  │  __init__.py
    │  │      │      │  │  
    │  │      │      │  ├─cli
    │  │      │      │  │      chardetect.py
    │  │      │      │  │      __init__.py
    │  │      │      │  │      
    │  │      │      │  └─metadata
    │  │      │      │          languages.py
    │  │      │      │          __init__.py
    │  │      │      │          
    │  │      │      ├─colorama
    │  │      │      │      ansi.py
    │  │      │      │      ansitowin32.py
    │  │      │      │      initialise.py
    │  │      │      │      win32.py
    │  │      │      │      winterm.py
    │  │      │      │      __init__.py
    │  │      │      │      
    │  │      │      ├─distlib
    │  │      │      │  │  compat.py
    │  │      │      │  │  database.py
    │  │      │      │  │  index.py
    │  │      │      │  │  locators.py
    │  │      │      │  │  manifest.py
    │  │      │      │  │  markers.py
    │  │      │      │  │  metadata.py
    │  │      │      │  │  resources.py
    │  │      │      │  │  scripts.py
    │  │      │      │  │  t32.exe
    │  │      │      │  │  t64.exe
    │  │      │      │  │  util.py
    │  │      │      │  │  version.py
    │  │      │      │  │  w32.exe
    │  │      │      │  │  w64.exe
    │  │      │      │  │  wheel.py
    │  │      │      │  │  __init__.py
    │  │      │      │  │  
    │  │      │      │  └─_backport
    │  │      │      │          misc.py
    │  │      │      │          shutil.py
    │  │      │      │          sysconfig.cfg
    │  │      │      │          sysconfig.py
    │  │      │      │          tarfile.py
    │  │      │      │          __init__.py
    │  │      │      │          
    │  │      │      ├─html5lib
    │  │      │      │  │  constants.py
    │  │      │      │  │  html5parser.py
    │  │      │      │  │  serializer.py
    │  │      │      │  │  _ihatexml.py
    │  │      │      │  │  _inputstream.py
    │  │      │      │  │  _tokenizer.py
    │  │      │      │  │  _utils.py
    │  │      │      │  │  __init__.py
    │  │      │      │  │  
    │  │      │      │  ├─filters
    │  │      │      │  │      alphabeticalattributes.py
    │  │      │      │  │      base.py
    │  │      │      │  │      inject_meta_charset.py
    │  │      │      │  │      lint.py
    │  │      │      │  │      optionaltags.py
    │  │      │      │  │      sanitizer.py
    │  │      │      │  │      whitespace.py
    │  │      │      │  │      __init__.py
    │  │      │      │  │      
    │  │      │      │  ├─treeadapters
    │  │      │      │  │      genshi.py
    │  │      │      │  │      sax.py
    │  │      │      │  │      __init__.py
    │  │      │      │  │      
    │  │      │      │  ├─treebuilders
    │  │      │      │  │      base.py
    │  │      │      │  │      dom.py
    │  │      │      │  │      etree.py
    │  │      │      │  │      etree_lxml.py
    │  │      │      │  │      __init__.py
    │  │      │      │  │      
    │  │      │      │  ├─treewalkers
    │  │      │      │  │      base.py
    │  │      │      │  │      dom.py
    │  │      │      │  │      etree.py
    │  │      │      │  │      etree_lxml.py
    │  │      │      │  │      genshi.py
    │  │      │      │  │      __init__.py
    │  │      │      │  │      
    │  │      │      │  └─_trie
    │  │      │      │          py.py
    │  │      │      │          _base.py
    │  │      │      │          __init__.py
    │  │      │      │          
    │  │      │      ├─idna
    │  │      │      │      codec.py
    │  │      │      │      compat.py
    │  │      │      │      core.py
    │  │      │      │      idnadata.py
    │  │      │      │      intranges.py
    │  │      │      │      package_data.py
    │  │      │      │      uts46data.py
    │  │      │      │      __init__.py
    │  │      │      │      
    │  │      │      ├─msgpack
    │  │      │      │      exceptions.py
    │  │      │      │      ext.py
    │  │      │      │      fallback.py
    │  │      │      │      _version.py
    │  │      │      │      __init__.py
    │  │      │      │      
    │  │      │      ├─packaging
    │  │      │      │      markers.py
    │  │      │      │      requirements.py
    │  │      │      │      specifiers.py
    │  │      │      │      tags.py
    │  │      │      │      utils.py
    │  │      │      │      version.py
    │  │      │      │      _compat.py
    │  │      │      │      _structures.py
    │  │      │      │      _typing.py
    │  │      │      │      __about__.py
    │  │      │      │      __init__.py
    │  │      │      │      
    │  │      │      ├─pep517
    │  │      │      │  │  build.py
    │  │      │      │  │  check.py
    │  │      │      │  │  colorlog.py
    │  │      │      │  │  compat.py
    │  │      │      │  │  dirtools.py
    │  │      │      │  │  envbuild.py
    │  │      │      │  │  meta.py
    │  │      │      │  │  wrappers.py
    │  │      │      │  │  __init__.py
    │  │      │      │  │  
    │  │      │      │  └─in_process
    │  │      │      │          _in_process.py
    │  │      │      │          __init__.py
    │  │      │      │          
    │  │      │      ├─pkg_resources
    │  │      │      │      py31compat.py
    │  │      │      │      __init__.py
    │  │      │      │      
    │  │      │      ├─progress
    │  │      │      │      bar.py
    │  │      │      │      counter.py
    │  │      │      │      spinner.py
    │  │      │      │      __init__.py
    │  │      │      │      
    │  │      │      ├─requests
    │  │      │      │      adapters.py
    │  │      │      │      api.py
    │  │      │      │      auth.py
    │  │      │      │      certs.py
    │  │      │      │      compat.py
    │  │      │      │      cookies.py
    │  │      │      │      exceptions.py
    │  │      │      │      help.py
    │  │      │      │      hooks.py
    │  │      │      │      models.py
    │  │      │      │      packages.py
    │  │      │      │      sessions.py
    │  │      │      │      status_codes.py
    │  │      │      │      structures.py
    │  │      │      │      utils.py
    │  │      │      │      _internal_utils.py
    │  │      │      │      __init__.py
    │  │      │      │      __version__.py
    │  │      │      │      
    │  │      │      ├─resolvelib
    │  │      │      │  │  providers.py
    │  │      │      │  │  reporters.py
    │  │      │      │  │  resolvers.py
    │  │      │      │  │  structs.py
    │  │      │      │  │  __init__.py
    │  │      │      │  │  
    │  │      │      │  └─compat
    │  │      │      │          collections_abc.py
    │  │      │      │          __init__.py
    │  │      │      │          
    │  │      │      ├─tenacity
    │  │      │      │      after.py
    │  │      │      │      before.py
    │  │      │      │      before_sleep.py
    │  │      │      │      compat.py
    │  │      │      │      nap.py
    │  │      │      │      retry.py
    │  │      │      │      stop.py
    │  │      │      │      tornadoweb.py
    │  │      │      │      wait.py
    │  │      │      │      _asyncio.py
    │  │      │      │      _utils.py
    │  │      │      │      __init__.py
    │  │      │      │      
    │  │      │      ├─toml
    │  │      │      │      decoder.py
    │  │      │      │      encoder.py
    │  │      │      │      ordered.py
    │  │      │      │      tz.py
    │  │      │      │      __init__.py
    │  │      │      │      
    │  │      │      ├─urllib3
    │  │      │      │  │  connection.py
    │  │      │      │  │  connectionpool.py
    │  │      │      │  │  exceptions.py
    │  │      │      │  │  fields.py
    │  │      │      │  │  filepost.py
    │  │      │      │  │  poolmanager.py
    │  │      │      │  │  request.py
    │  │      │      │  │  response.py
    │  │      │      │  │  _collections.py
    │  │      │      │  │  _version.py
    │  │      │      │  │  __init__.py
    │  │      │      │  │  
    │  │      │      │  ├─contrib
    │  │      │      │  │  │  appengine.py
    │  │      │      │  │  │  ntlmpool.py
    │  │      │      │  │  │  pyopenssl.py
    │  │      │      │  │  │  securetransport.py
    │  │      │      │  │  │  socks.py
    │  │      │      │  │  │  _appengine_environ.py
    │  │      │      │  │  │  __init__.py
    │  │      │      │  │  │  
    │  │      │      │  │  └─_securetransport
    │  │      │      │  │          bindings.py
    │  │      │      │  │          low_level.py
    │  │      │      │  │          __init__.py
    │  │      │      │  │          
    │  │      │      │  ├─packages
    │  │      │      │  │  │  six.py
    │  │      │      │  │  │  __init__.py
    │  │      │      │  │  │  
    │  │      │      │  │  ├─backports
    │  │      │      │  │  │      makefile.py
    │  │      │      │  │  │      __init__.py
    │  │      │      │  │  │      
    │  │      │      │  │  └─ssl_match_hostname
    │  │      │      │  │          _implementation.py
    │  │      │      │  │          __init__.py
    │  │      │      │  │          
    │  │      │      │  └─util
    │  │      │      │          connection.py
    │  │      │      │          proxy.py
    │  │      │      │          queue.py
    │  │      │      │          request.py
    │  │      │      │          response.py
    │  │      │      │          retry.py
    │  │      │      │          ssltransport.py
    │  │      │      │          ssl_.py
    │  │      │      │          timeout.py
    │  │      │      │          url.py
    │  │      │      │          wait.py
    │  │      │      │          __init__.py
    │  │      │      │          
    │  │      │      └─webencodings
    │  │      │              labels.py
    │  │      │              mklabels.py
    │  │      │              tests.py
    │  │      │              x_user_defined.py
    │  │      │              __init__.py
    │  │      │              
    │  │      ├─pip-21.1.2.dist-info
    │  │      │      entry_points.txt
    │  │      │      INSTALLER
    │  │      │      LICENSE.txt
    │  │      │      METADATA
    │  │      │      RECORD
    │  │      │      top_level.txt
    │  │      │      WHEEL
    │  │      │      
    │  │      ├─pkg_resources
    │  │      │  │  __init__.py
    │  │      │  │  
    │  │      │  ├─extern
    │  │      │  │      __init__.py
    │  │      │  │      
    │  │      │  ├─tests
    │  │      │  │  └─data
    │  │      │  │      └─my-test-package-source
    │  │      │  │              setup.py
    │  │      │  │              
    │  │      │  └─_vendor
    │  │      │      │  appdirs.py
    │  │      │      │  pyparsing.py
    │  │      │      │  __init__.py
    │  │      │      │  
    │  │      │      └─packaging
    │  │      │              markers.py
    │  │      │              requirements.py
    │  │      │              specifiers.py
    │  │      │              tags.py
    │  │      │              utils.py
    │  │      │              version.py
    │  │      │              _compat.py
    │  │      │              _structures.py
    │  │      │              _typing.py
    │  │      │              __about__.py
    │  │      │              __init__.py
    │  │      │              
    │  │      ├─setuptools
    │  │      │  │  archive_util.py
    │  │      │  │  build_meta.py
    │  │      │  │  cli-32.exe
    │  │      │  │  cli-64.exe
    │  │      │  │  cli.exe
    │  │      │  │  config.py
    │  │      │  │  depends.py
    │  │      │  │  dep_util.py
    │  │      │  │  dist.py
    │  │      │  │  errors.py
    │  │      │  │  extension.py
    │  │      │  │  glob.py
    │  │      │  │  gui-32.exe
    │  │      │  │  gui-64.exe
    │  │      │  │  gui.exe
    │  │      │  │  installer.py
    │  │      │  │  launch.py
    │  │      │  │  lib2to3_ex.py
    │  │      │  │  monkey.py
    │  │      │  │  msvc.py
    │  │      │  │  namespaces.py
    │  │      │  │  package_index.py
    │  │      │  │  py34compat.py
    │  │      │  │  sandbox.py
    │  │      │  │  script (dev).tmpl
    │  │      │  │  script.tmpl
    │  │      │  │  ssl_support.py
    │  │      │  │  unicode_utils.py
    │  │      │  │  version.py
    │  │      │  │  wheel.py
    │  │      │  │  windows_support.py
    │  │      │  │  _deprecation_warning.py
    │  │      │  │  _imp.py
    │  │      │  │  __init__.py
    │  │      │  │  
    │  │      │  ├─command
    │  │      │  │      alias.py
    │  │      │  │      bdist_egg.py
    │  │      │  │      bdist_rpm.py
    │  │      │  │      build_clib.py
    │  │      │  │      build_ext.py
    │  │      │  │      build_py.py
    │  │      │  │      develop.py
    │  │      │  │      dist_info.py
    │  │      │  │      easy_install.py
    │  │      │  │      egg_info.py
    │  │      │  │      install.py
    │  │      │  │      install_egg_info.py
    │  │      │  │      install_lib.py
    │  │      │  │      install_scripts.py
    │  │      │  │      launcher manifest.xml
    │  │      │  │      py36compat.py
    │  │      │  │      register.py
    │  │      │  │      rotate.py
    │  │      │  │      saveopts.py
    │  │      │  │      sdist.py
    │  │      │  │      setopt.py
    │  │      │  │      test.py
    │  │      │  │      upload.py
    │  │      │  │      upload_docs.py
    │  │      │  │      __init__.py
    │  │      │  │      
    │  │      │  ├─extern
    │  │      │  │      __init__.py
    │  │      │  │      
    │  │      │  ├─_distutils
    │  │      │  │  │  archive_util.py
    │  │      │  │  │  bcppcompiler.py
    │  │      │  │  │  ccompiler.py
    │  │      │  │  │  cmd.py
    │  │      │  │  │  config.py
    │  │      │  │  │  core.py
    │  │      │  │  │  cygwinccompiler.py
    │  │      │  │  │  debug.py
    │  │      │  │  │  dep_util.py
    │  │      │  │  │  dir_util.py
    │  │      │  │  │  dist.py
    │  │      │  │  │  errors.py
    │  │      │  │  │  extension.py
    │  │      │  │  │  fancy_getopt.py
    │  │      │  │  │  filelist.py
    │  │      │  │  │  file_util.py
    │  │      │  │  │  log.py
    │  │      │  │  │  msvc9compiler.py
    │  │      │  │  │  msvccompiler.py
    │  │      │  │  │  py35compat.py
    │  │      │  │  │  py38compat.py
    │  │      │  │  │  spawn.py
    │  │      │  │  │  sysconfig.py
    │  │      │  │  │  text_file.py
    │  │      │  │  │  unixccompiler.py
    │  │      │  │  │  util.py
    │  │      │  │  │  version.py
    │  │      │  │  │  versionpredicate.py
    │  │      │  │  │  _msvccompiler.py
    │  │      │  │  │  __init__.py
    │  │      │  │  │  
    │  │      │  │  └─command
    │  │      │  │          bdist.py
    │  │      │  │          bdist_dumb.py
    │  │      │  │          bdist_msi.py
    │  │      │  │          bdist_rpm.py
    │  │      │  │          bdist_wininst.py
    │  │      │  │          build.py
    │  │      │  │          build_clib.py
    │  │      │  │          build_ext.py
    │  │      │  │          build_py.py
    │  │      │  │          build_scripts.py
    │  │      │  │          check.py
    │  │      │  │          clean.py
    │  │      │  │          config.py
    │  │      │  │          install.py
    │  │      │  │          install_data.py
    │  │      │  │          install_egg_info.py
    │  │      │  │          install_headers.py
    │  │      │  │          install_lib.py
    │  │      │  │          install_scripts.py
    │  │      │  │          py37compat.py
    │  │      │  │          register.py
    │  │      │  │          sdist.py
    │  │      │  │          upload.py
    │  │      │  │          __init__.py
    │  │      │  │          
    │  │      │  └─_vendor
    │  │      │      │  ordered_set.py
    │  │      │      │  pyparsing.py
    │  │      │      │  __init__.py
    │  │      │      │  
    │  │      │      ├─more_itertools
    │  │      │      │      more.py
    │  │      │      │      recipes.py
    │  │      │      │      __init__.py
    │  │      │      │      
    │  │      │      └─packaging
    │  │      │              markers.py
    │  │      │              requirements.py
    │  │      │              specifiers.py
    │  │      │              tags.py
    │  │      │              utils.py
    │  │      │              version.py
    │  │      │              _compat.py
    │  │      │              _structures.py
    │  │      │              _typing.py
    │  │      │              __about__.py
    │  │      │              __init__.py
    │  │      │              
    │  │      ├─setuptools-57.0.0.dist-info
    │  │      │      dependency_links.txt
    │  │      │      entry_points.txt
    │  │      │      INSTALLER
    │  │      │      LICENSE
    │  │      │      METADATA
    │  │      │      RECORD
    │  │      │      top_level.txt
    │  │      │      WHEEL
    │  │      │      
    │  │      ├─wheel
    │  │      │  │  bdist_wheel.py
    │  │      │  │  macosx_libfile.py
    │  │      │  │  metadata.py
    │  │      │  │  pkginfo.py
    │  │      │  │  util.py
    │  │      │  │  wheelfile.py
    │  │      │  │  __init__.py
    │  │      │  │  __main__.py
    │  │      │  │  
    │  │      │  ├─cli
    │  │      │  │      convert.py
    │  │      │  │      pack.py
    │  │      │  │      unpack.py
    │  │      │  │      __init__.py
    │  │      │  │      
    │  │      │  └─vendored
    │  │      │      │  __init__.py
    │  │      │      │  
    │  │      │      └─packaging
    │  │      │              tags.py
    │  │      │              _typing.py
    │  │      │              __init__.py
    │  │      │              
    │  │      ├─wheel-0.36.2.dist-info
    │  │      │      entry_points.txt
    │  │      │      INSTALLER
    │  │      │      LICENSE.txt
    │  │      │      METADATA
    │  │      │      RECORD
    │  │      │      top_level.txt
    │  │      │      WHEEL
    │  │      │      
    │  │      └─_distutils_hack
    │  │              override.py
    │  │              __init__.py
    │  │              
    │  └─Scripts
    │          activate
    │          activate.bat
    │          activate.fish
    │          activate.ps1
    │          activate.xsh
    │          activate_this.py
    │          deactivate.bat
    │          pip-3.10.exe
    │          pip.exe
    │          pip3.10.exe
    │          pip3.exe
    │          pydoc.bat
    │          python.exe
    │          pythonw.exe
    │          wheel-3.10.exe
    │          wheel.exe
    │          wheel3.10.exe
    │          wheel3.exe
    │          
    ├─实训01
    │      BOX_OFFICE.py
    │      company.html
    │      data_analysis.py
    │      debug.py
    │      doubanTop250.py
    │      img.png
    │      maoyan_film.py
    │      movie.db
    │      movieCompany.db
    │      movieTop2016_2022.db
    │      my.html
    │      my_specific.html
    │      office_box.html
    │      Readme
    │      resource
    │      test.db
    │      test_01.py
    │      The_most_profitable_film_company.py
    │      豆瓣TOP250.xls
    │      
    └─实训02
            2016~2022Top100电影发布年份图.html
            2016~2022Top电影矩形树状图.html
            2016年电影TOP15柱状图.html
            2017年电影TOP15柱状图.html
            2018年电影TOP15柱状图.html
            2019年电影TOP15柱状图.html
            2020年电影TOP15柱状图.html
            2021年电影TOP15柱状图.html
            2022年电影TOP15柱状图.html
            Compare2016~2022.html
            debug_01.py
            movieTop2016_2022.db
            Movie_year_Compare.py
            nested_pies.html
            pd_pyrcharts_selflearning.py
            presentation.py
            ReadMe
            render.html
            show_info2016~2022.py
            Top15Company.html
            Top15电影制作公司.py
            word.jpg
            yearGainCompare.py
            yearMovieCompare.py
            
```

