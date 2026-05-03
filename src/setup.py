from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.AutomaticVolumeAdjustment'
setup(name='enigma2-plugin-systemplugins-automaticvolumeadjustment',
       version='1.0',
       description='AutomaticVolumeAdjustment',
       package_dir={pkg: 'AutomaticVolumeAdjustment'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
