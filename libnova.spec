%define debug_package          %{nil}
%define api	0.15
%define major	0
%define libname	%mklibname nova %{api} %{major}
%define devname %mklibname nova %{api} -d

Summary:	General purpose astronomy & astrodynamics library
Name:		libnova
Version:	0.15.0
Release:	4
Group:		Sciences/Astronomy
License:	LGPLv2+
Url:		http://sourceforge.net/projects/libnova/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

%description
Libnova is a general purpose, double precision, celestial mechanics, 
astrometry and astrodynamics library

%package -n %{libname}
Summary:	Library files for %{name}
Group:		Development/KDE and Qt

%description -n %{libname}
Contains library files for nova.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name} < 0.15.0-2

%description -n %{devname}
Contains library and header files for nova.

%prep
%setup -q
autoreconf -fi

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libnova-%{api}.so.%{major}*

%files -n %{devname}
%doc examples/*.c
%doc ChangeLog README AUTHORS NEWS COPYING
%{_bindir}/libnovaconfig
%{_includedir}/libnova
%{_libdir}/libnova.so

