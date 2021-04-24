#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gensim
Version  : 4.0.1
Release  : 53
URL      : https://files.pythonhosted.org/packages/1f/6c/363d00aa23642f42b27b908c6474ab981c75882eefc084210d5b8ce8cd8e/gensim-4.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/1f/6c/363d00aa23642f42b27b908c6474ab981c75882eefc084210d5b8ce8cd8e/gensim-4.0.1.tar.gz
Summary  : Python framework for fast Vector Space Modelling
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1-only
Requires: gensim-license = %{version}-%{release}
Requires: gensim-python = %{version}-%{release}
Requires: gensim-python3 = %{version}-%{release}
Requires: Pyro4
Requires: dataclasses
Requires: numpy
Requires: scipy
Requires: smart_open
BuildRequires : Cython
BuildRequires : Pyro4
BuildRequires : buildreq-distutils3
BuildRequires : dataclasses
BuildRequires : numpy
BuildRequires : python3-dev
BuildRequires : scipy
BuildRequires : smart_open

%description
==============================================
        gensim -- Topic Modelling in Python
        ==============================================
        
        |Travis|_
        |Wheel|_

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
Provides: pypi(gensim)
Requires: pypi(numpy)
Requires: pypi(scipy)
Requires: pypi(smart_open)

%description python3
python3 components for the gensim package.


%prep
%setup -q -n gensim-4.0.1
cd %{_builddir}/gensim-4.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617304395
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gensim
cp %{_builddir}/gensim-4.0.1/COPYING %{buildroot}/usr/share/package-licenses/gensim/01a6b4bf79aca9b556822601186afab86e8c4fbf
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gensim/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
