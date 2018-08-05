#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gensim
Version  : 3.5.0
Release  : 28
URL      : https://files.pythonhosted.org/packages/d1/8d/f20e715f3eae5a277b13a31d440d65f294fadbc2047c4d02226e1de05b6e/gensim-3.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d1/8d/f20e715f3eae5a277b13a31d440d65f294fadbc2047c4d02226e1de05b6e/gensim-3.5.0.tar.gz
Summary  : Python framework for fast Vector Space Modelling
Group    : Development/Tools
License  : LGPL-2.1
Requires: gensim-python3
Requires: gensim-license
Requires: gensim-python
Requires: numpy
Requires: pytest-rerunfailures
Requires: scikit-learn
Requires: scipy
Requires: six
Requires: smart_open
Requires: tensorflow
BuildRequires : Cython
BuildRequires : buildreq-distutils3
BuildRequires : numpy
BuildRequires : scipy
BuildRequires : six
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
%setup -q -n gensim-3.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533509167
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/gensim
cp COPYING %{buildroot}/usr/share/doc/gensim/COPYING
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/gensim/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
