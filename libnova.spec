%define libname %mklibname nova
%define devname %mklibname nova -d

Summary:	General purpose astronomy and astrodynamics library
Name:		libnova
Version:	0.15.0
Release:	13
Group:		Sciences/Astronomy
License:	LGPLv2+
URL:		https://sourceforge.net/projects/libnova/
Source0:	https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildSystem:	autotools
BuildRequires:	automake

%patchlist
libnova-0.15.0-cflags.patch

%description
Libnova is a general purpose, double precision, celestial mechanics,
astrometry and astrodynamics library.

%package -n %{libname}
Summary:	Library files for %{name}
Group:		System/Libraries
# The 0.15 in the old name is the upstream -release tag, not a soname split.
Provides:	%{_lib}nova0.15_0 = %{EVRD}
Provides:	%{name} = %{EVRD}
Obsoletes:	%{_lib}nova0.15_0 < %{EVRD}
Obsoletes:	%{name} < 0.15.0-2

%description -n %{libname}
Contains library files for nova.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	%{_lib}nova0.15-devel = %{EVRD}
Obsoletes:	%{_lib}nova0.15-devel < %{EVRD}

%description -n %{devname}
Contains library and header files for nova.

%prep
%autosetup -p1
autoconf

%files -n %{libname}
%{_libdir}/libnova-0.15.so.*

%files -n %{devname}
%doc examples/*.c
%doc ChangeLog README AUTHORS NEWS COPYING
%{_bindir}/libnovaconfig
%{_includedir}/libnova
%{_libdir}/libnova.so
