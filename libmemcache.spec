Summary:	libmemcache is the C API for memcached
Name:		libmemcache
Version:	1.2.4
Release:	0.2
Epoch:		0
License:	MIT
Group:		Libraries
Source0:	http://people.freebsd.org/~seanc/libmemcache/%{name}-%{version}.tar.bz2
# Source0-md5:	1b4dada8c7176fb018b489e09e6964f1
Patch0:		%{name}-install.patch
URL:		http://people.freebsd.org/~seanc/libmemcache/
BuildRequires:	pmk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Features
- Support for Multiple Memory Contexts. This is primarily used for
  programs that need to use memcache(3) inside of Apache where both
  Apache and PHP have their own memory management systems.
- Callback Interface. Using the callback interface, it's possible to
  lump many gets together into a single get request with a great deal
  of ease.
- Multiple Client Side Hashes. memcache(3) supports multiple hashing
  methods to distribute load across multiple servers.
- Multiple Servers. memcache(3) supports multiple servers.
- Support for Garbage Collection. memcache(3) was written with the
  Bohem Garbage Collector in mind.
- MIT Licensed. memcache(3) is as Open Source as it gets and can be
  embedded in anything (commercial software, open source, etc). May
  the GPL and its users rot in hell for their stupidity.

%package devel
Summary:	Development libraries and header files for libmemcache library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the development libraries and header
files for libmemcache.

%package static
Summary:	Static ... library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library for libmemcache.

%prep
%setup -q
%patch0 -p1

%build
pmk %{?debug:-e debug}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="-std=c99 %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog INSTALL
%attr(755,root,root) %{_libdir}/libmemcache.so.*.*

%files devel
%doc regress.c
%defattr(644,root,root,755)
%{_includedir}/memcache.h
%attr(755,root,root) %{_libdir}/libmemcache.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libmemcache.a
