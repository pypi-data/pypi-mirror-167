#!/bin/csh
setenv TBBROOT "D:\a\scikit-stan\scikit-stan\build\lib.win-amd64-cpython-37\scikit_stan\stan_files\cmdstan-2.30.1\stan\lib\stan_math\lib\tbb_2020.3"
setenv TBB_ARCH_PLATFORM "intel64\mingw8.3.0"
setenv TBB_TARGET_ARCH "intel64"
setenv CPATH "${TBBROOT}\include;$CPATH"
setenv LIBRARY_PATH "D:\a\scikit-stan\scikit-stan\build\lib.win-amd64-cpython-37\scikit_stan\stan_files\cmdstan-2.30.1\stan\lib\stan_math\lib\tbb;$LIBRARY_PATH"
setenv PATH "D:\a\scikit-stan\scikit-stan\build\lib.win-amd64-cpython-37\scikit_stan\stan_files\cmdstan-2.30.1\stan\lib\stan_math\lib\tbb;$PATH"
setenv LD_LIBRARY_PATH "D:\a\scikit-stan\scikit-stan\build\lib.win-amd64-cpython-37\scikit_stan\stan_files\cmdstan-2.30.1\stan\lib\stan_math\lib\tbb;$LD_LIBRARY_PATH"
