%global commit eae1e8b9d12468059bdd7dee893508e470fa83d8
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       xavs2
Version:    1.3
Release:    1%{?dist}
Summary:    An open-source encoder of AVS2-P2/IEEE1857.4 video coding standard
URL:        https://github.com/pkuvcl/xavs2
License:    GPLv2

Source:	    https://github.com/pkuvcl/xavs2/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  nasm >= 2.13
Requires:   %{name}-libs = %{version}-%{release}

%description
xavs2 is an open-source encoder of AVS2-P2/IEEE1857.4 video coding standard.

This package contains the command line encoder.

%package libs
Summary:    AVS2-P2/IEEE1857.4 encoder library

%description libs
davs2 is an open-source encoder of AVS2-P2/IEEE1857.4 video coding standard.

This package contains the shared library.

%package devel
Summary:    AVS2-P2/IEEE1857.4 encoder library development files
Requires:   %{name} = %{version}-%{release}

%description devel
davs2 is an open-source encoder of AVS2-P2/IEEE1857.4 video coding standard.

This package contains the shared library development files.

%prep
%autosetup -n %{name}-%{commit}

%build
cd build/linux
%configure \
    --bit-depth='8' \
    --chroma-format='all' \
    --disable-static \
    --enable-pic \
    --enable-shared

%make_build

%install
cd build/linux
%make_install install-cli install-lib-shared

find %{buildroot} -name "*a" -delete


%files
%license COPYING
%doc README.md
%{_bindir}/%{name}

%files libs
%{_libdir}/lib%{name}.so.13

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}_config.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog

* Thu Jul 11 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.3-1
- Initial build.
