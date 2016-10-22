%{?scl:%scl_package nodejs-balanced-match}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global packagename balanced-match
%global enable_tests 0
# tests disabled to to reliance on ancient version of 'tape'

Name:		%{?scl_prefix}nodejs-balanced-match
Version:	0.2.1
Release:	4%{?dist}
Summary:	Match balanced character pairs, like "{" and "}"

License:	MIT
URL:		https://github.com/juliangruber/balanced-match.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

ExclusiveArch:	%{ix86} x86_64 %{arm} noarch
BuildArch:	noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}mocha
%endif

Requires:	%{?scl_prefix}nodejs

%description
Match balanced character pairs, like "{" and "}"

%prep
%setup -q -n package
# setup the tests
#%setup -q -T -D -a 1 -n package

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
%{?scl:scl enable %{scl} - << \EOF}
make test
%{?scl:EOF}
%endif

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%doc LICENSE.md
%{nodejs_sitelib}/%{packagename}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.2.1-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.2.1-3
- Rebuilt with updated metapackage

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 0.2.1-2
- Enable scl macros

* Tue Oct 20 2015 Jared Smith <jsmith@fedoraproject.org> - 0.2.0-1
- Initial packaging
