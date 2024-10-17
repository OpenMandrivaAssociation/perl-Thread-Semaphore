%define upstream_name    Thread-Semaphore
%define upstream_version 2.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Thread-safe semaphores
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Thread/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(threads::shared)
BuildArch:	noarch

%description
Semaphores provide a mechanism to regulate access to resources. Unlike
locks, semaphores aren't tied to particular scalars, and so may be used to
control access to anything you care to use them for.

Semaphores don't limit their values to zero and one, so they can be used to
control access to some resource that there may be more than one of (e.g.,
filehandles). Increment and decrement amounts aren't fixed at one either,
so threads can reserve or return multiple resources at once.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.120.0-2mdv2011.0
+ Revision: 656976
- rebuild for updated spec-helper

* Sun Dec 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.120.0-1mdv2011.0
+ Revision: 625284
- update to new version 2.12

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.110.0-4mdv2011.0
+ Revision: 597203
- rebuild

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 2.110.0-3mdv2011.0
+ Revision: 562437
- rebuild

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 2.110.0-2mdv2011.0
+ Revision: 561027
- rebuild

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.110.0-1mdv2011.0
+ Revision: 552247
- update to 2.11

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2.90.0-1mdv2010.0
+ Revision: 401506
- rebuild using %%perl_convert_version
- fixed license field

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 2.09-1mdv2010.0
+ Revision: 374410
- import perl-Thread-Semaphore


* Mon May 11 2009 cpan2dist 2.09-1mdv
- initial mdv release, generated with cpan2dist

