Name:           yaml-cpp
Version:        0.6.3
Release:        1
Summary:        A YAML parser and emitter for C++
Group:          Development/Libraries
License:        MIT
URL:            http://code.google.com/p/yaml-cpp/
Source0:        http://yaml-cpp.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  sed
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
License:        MIT
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig
Requires:       boost-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Static library for %{name}
Group:          Development/Libraries
License:        MIT
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}

%description    static
The %{name}-static package contains the static library for %{name}.

%prep
%setup -q  -n %{name}-%{version}/upstream

%build
export CC=gcc
export CXX=g++
%cmake -DYAML_CPP_BUILD_TESTS:BOOL=OFF \
       -DCMAKE_C_COMPILER=$CC \
       -DCMAKE_CXX_COMPILER=$CXX \
       -DBUILD_SHARED_LIBS=OFF
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc license.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/yaml-cpp/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files static
%license license.txt
%{_libdir}/*.a
