#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gensim
Version  : 3.3.0
Release  : 26
URL      : http://pypi.debian.net/gensim/gensim-3.3.0.tar.gz
Source0  : http://pypi.debian.net/gensim/gensim-3.3.0.tar.gz
Summary  : Python framework for fast Vector Space Modelling
Group    : Development/Tools
License  : LGPL-2.1
Requires: gensim-python3
Requires: gensim-python
Requires: numpy
Requires: scikit-learn
Requires: scipy
Requires: six
Requires: smart_open
Requires: tensorflow
BuildRequires : Cython
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : scipy
BuildRequires : setuptools
BuildRequires : six
BuildRequires : smart_open

%description
==============================================
        gensim -- Topic Modelling in Python
        ==============================================
        
        |Travis|_
        |Wheel|_

%package python
Summary: python components for the gensim package.
Group: Default
Requires: gensim-python3

%description python
python components for the gensim package.


%package python3
Summary: python3 components for the gensim package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gensim package.


%prep
%setup -q -n gensim-3.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528564391
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
