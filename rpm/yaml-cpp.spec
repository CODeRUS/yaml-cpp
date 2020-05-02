Name:           yaml-cpp
Version:        0.6.3
Release:        1
Summary:        A YAML parser and emitter for C++
Group:          Development/Libraries
License:        MIT
URL:            http://code.google.com/p/yaml-cpp/
Source0:        http://yaml-cpp.googlecode.com/files/%{name}-%{version}.tar.gz
# Make yaml-cpp compatible with boost 1.67+
Patch1:         yaml-cpp-boost-1.67.diff

BuildRequires:  cmake
BuildRequires:  boost-devel
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
### Build shared libraries
mkdir build-shared
pushd build-shared
    # ask cmake to not strip binaries
    %cmake -DYAML_CPP_BUILD_TOOLS=0 \
           -DBUILD_SHARED_LIBS=ON \
           ../
    %make_build
popd

### Build static libraries
mkdir build-static
pushd build-static
    # ask cmake to not strip binaries
    %cmake -DYAML_CPP_BUILD_TOOLS=0 \
           -DBUILD_SHARED_LIBS=OFF \
           -DYAML_CPP_BUILD_CONTRIB=OFF \
           ../
    %make_build
popd


%install
pushd build-shared
    %make_install
popd

pushd build-static
    %make_install
popd


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
