#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	inc
%define		pnam	latest
Summary:	inc::latest - use modules bundled in inc/ if they are newer than installed ones
Summary(pl.UTF-8):	inc-latest - użycie modułów dołączonych w inc/ jeśli są nowsze od zainstalowanych
Name:		perl-inc-latest
Version:	0.500
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DA/DAGOLDEN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d1e0deb52bcc9f9b0f990ceb077a8ffd
URL:		https://metacpan.org/release/inc-latest
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.17
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WARNING -- THIS IS AN EXPERIMENTAL MODULE. It was originally bundled
(as an experiment) with Module::Build and has been split out for more
general use.

The inc::latest module helps bootstrap configure-time dependencies for
CPAN distributions. These dependencies get bundled into the inc
directory within a distribution and are used by Makefile.PL or
Build.PL.

%description -l pl.UTF-8
UWAGA: TEN MODUŁ JEST EKSPERYMENTALNY. Oryginalnie był dołączany (jako
eksperyment) do Module::Build, następnie został wydzielony do bardziej
ogólnego użytku.

Moduł inc::latest pomaga przy bootstrapowaniu zależności czasu
konfiguracji dla pakietów CPAN. Zależności te są dołączane do katalogu
inc wewnątrz pakieut, a następnie używane przez Makefile.PL lub
Build.PL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/inc/latest.pm
%{perl_vendorlib}/inc/latest
%{_mandir}/man3/inc::latest*.3pm*
