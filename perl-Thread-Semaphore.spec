%define upstream_name    Thread-Semaphore
%define upstream_version 2.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Thread-safe semaphores
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Thread/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(threads::shared)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

