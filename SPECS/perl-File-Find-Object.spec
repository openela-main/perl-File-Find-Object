Name:           perl-File-Find-Object
Version:        0.3.2
Release:        5%{?dist}
Summary:        Object oriented File::Find replacement
License:        GPLv2+ or Artistic 2.0
URL:            http://search.cpan.org/dist/File-Find-Object/
Source0:        http://www.cpan.org/authors/id/S/SH/SHLOMIF/File-Find-Object-v%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(integer)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
File::Find::Object does the same job as File::Find but works like an object
and with an iterator. As File::Find is not object oriented, one cannot
perform multiple searches in the same application. The second problem of
File::Find is its file processing: after starting its main loop, one cannot
easily wait for another event and so get the next result.

%prep
%setup -qn File-Find-Object-v%{version}
chmod -c 644 examples/tree

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README examples/
%{perl_vendorlib}/File/
%{_mandir}/man3/File::Find::Object.3*
%{_mandir}/man3/File::Find::Object::Base.3*
%{_mandir}/man3/File::Find::Object::PathComp.3*
%{_mandir}/man3/File::Find::Object::Result.3*

%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.2-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Paul Howarth <paul@city-fan.org> - 0.3.2-1
- Update to 0.3.2
  - Made the version number consistent across the .pm files
    (https://bitbucket.org/shlomif/perl-file-find-object/issues/1/wrong-version-number)

* Mon Jan  9 2017 Paul Howarth <paul@city-fan.org> - 0.3.1-1
- Update to 0.3.1
  - Fixed an issue with tracking the depth of the inodes when detecting a
    symlink loop

* Mon Sep 12 2016 Paul Howarth <paul@city-fan.org> - 0.3.0-1
- Update to 0.3.0
  - Converted the build system to Dist-Zilla
- Switch to ExtUtils::MakeMaker-based flow

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.13-5
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.13-4
- Perl 5.24 rebuild

* Mon Feb 29 2016 Paul Howarth <paul@city-fan.org> - 0.2.13-3
- Spec clean-up

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 24 2015 Petr Pisar <ppisar@redhat.com> - 0.2.13-1
- 0.2.13 bump
- License changed to (GPLv2+ or Artistic 2.0)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.11-6
- Perl 5.22 re-rebuild of bootstrapped packages

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.11-5
- Perl 5.22 rebuild

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.11-4
- Perl 5.20 re-rebuild of bootstrapped packages

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.11-3
- Perl 5.20 rebuild

* Wed Jul 23 2014 Petr Pisar <ppisar@redhat.com> - 0.2.11-2
- Break dependency cycle perl-File-Find-Object → perl-Test-TrailingSpace →
  perl-File-Find-Object-Rule

* Wed Jun 11 2014 Christopher Meng <rpm@cicku.me> - 0.2.11-1
- Update to 0.2.11

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.2.7-3
- Perl 5.18 rebuild

* Wed Jul 03 2013 Christopher Meng <rpm@cicku.me> - 0.2.7-2
- Fix the license.
- Fix the files permissions.
- Fill up the BRs.

* Sun May 26 2013 Christopher Meng <rpm@cicku.me> - 0.2.7-1
- Initial Package.
