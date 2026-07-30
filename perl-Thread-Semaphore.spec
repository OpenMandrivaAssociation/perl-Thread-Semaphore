%define upstream_name    Thread-Semaphore
%define upstream_version 2.13
Name:		perl-%{upstream_name}
Version:	2.13
Release:	1

Summary:	Thread-safe semaphores
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Thread-Semaphore
Source0:	https://cpan.metacpan.org/authors/id/J/JD/JDHEDDEN/Thread-Semaphore-2.13.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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

