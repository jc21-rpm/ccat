%global debug_package %{nil}
%global gh_user owenthereal

Name:          ccat
Version:       1.1.0
Release:       1
Summary:       ccat is the colorizing cat. It works similar to cat but displays content with syntax highlighting.
License:       MIT
URL:           https://github.com/%{gh_user}/%{name}
Source:        https://github.com/%{gh_user}/%{name}/releases/download/v%{version}/linux-amd64-%{version}.tar.gz

%description
Supported languages:
- JavaScript
- Java
- Ruby
- Python
- Go
- C
- JSON

%prep
%setup -q -n linux-amd64-%{version}

%install
install -Dm0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%doc LICENSE *.md

%changelog
* Fri Aug 31 2018 Jamie Curnow <jc@jc21.com> 1.1.0-1
- Initial spec
