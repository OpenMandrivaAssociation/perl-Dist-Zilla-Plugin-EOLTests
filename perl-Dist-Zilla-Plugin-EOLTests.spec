%define upstream_name    Dist-Zilla-Plugin-EOLTests
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Release tests making sure correct line endings are used
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Dist::Zilla::Plugin::InlineFiles)
BuildRequires:	perl(Dist::Zilla::Role::TextTemplate)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::EOL)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
This is an extension of the Dist::Zilla::Plugin::InlineFiles manpage,
providing the following files:

* *

  xt/release/eol.t

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

