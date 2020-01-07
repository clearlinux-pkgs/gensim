#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gensim
Version  : 3.8.1
Release  : 44
URL      : https://files.pythonhosted.org/packages/73/f2/e9af000df6419bf1a63ffed3e6033a1b1d8fcf2f971fcdac15296619aff8/gensim-3.8.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/73/f2/e9af000df6419bf1a63ffed3e6033a1b1d8fcf2f971fcdac15296619aff8/gensim-3.8.1.tar.gz
Summary  : Python framework for fast Vector Space Modelling
Group    : Development/Tools
License  : LGPL-2.1
Requires: gensim-license = %{version}-%{release}
Requires: gensim-python = %{version}-%{release}
Requires: gensim-python3 = %{version}-%{release}
Requires: Pyro4
Requires: numpy
Requires: scipy
Requires: six
Requires: smart_open
BuildRequires : Cython
BuildRequires : Pyro4
BuildRequires : buildreq-distutils3
BuildRequires : numpy
BuildRequires : scipy
BuildRequires : six
BuildRequires : smart_open

%description
gensim – Topic Modelling in Python
==================================
[![Build Status](https://travis-ci.org/RaRe-Technologies/gensim.svg?branch=develop)](https://travis-ci.org/RaRe-Technologies/gensim)
[![GitHub release](https://img.shields.io/github/release/rare-technologies/gensim.svg?maxAge=3600)](https://github.com/RaRe-Technologies/gensim/releases)
[![Conda-forge Build](https://anaconda.org/conda-forge/gensim/badges/version.svg)](https://anaconda.org/conda-forge/gensim)
[![Wheel](https://img.shields.io/pypi/wheel/gensim.svg)](https://pypi.python.org/pypi/gensim)
[![DOI](https://zenodo.org/badge/DOI/10.13140/2.1.2393.1847.svg)](https://doi.org/10.13140/2.1.2393.1847)
[![Mailing List](https://img.shields.io/badge/-Mailing%20List-brightgreen.svg)](https://groups.google.com/forum/#!forum/gensim)
[![Gitter](https://img.shields.io/badge/gitter-join%20chat%20%E2%86%92-09a3d5.svg)](https://gitter.im/RaRe-Technologies/gensim)
[![Follow](https://img.shields.io/twitter/follow/gensim_py.svg?style=social&label=Follow)](https://twitter.com/gensim_py)

%package license
Summary: license components for the gensim package.
Group: Default

%description license
license components for the gensim package.


%package python
Summary: python components for the gensim package.
Group: Default
Requires: gensim-python3 = %{version}-%{release}

%description python
python components for the gensim package.


%package python3
Summary: python3 components for the gensim package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gensim package.


%prep
%setup -q -n gensim-3.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569591718
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gensim
cp COPYING %{buildroot}/usr/share/package-licenses/gensim/COPYING
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gensim/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
