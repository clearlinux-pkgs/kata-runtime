#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kata-runtime
Version  : 1.8.2
Release  : 47
URL      : https://github.com/kata-containers/runtime/archive/1.8.2/runtime-1.8.2.tar.gz
Source0  : https://github.com/kata-containers/runtime/archive/1.8.2/runtime-1.8.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-SA-4.0 ISC MIT MPL-2.0 MPL-2.0-no-copyleft-exception
Requires: kata-runtime-bin = %{version}-%{release}
Requires: kata-runtime-data = %{version}-%{release}
Requires: kata-runtime-libexec = %{version}-%{release}
Requires: kata-runtime-license = %{version}-%{release}
Requires: kata-runtime-services = %{version}-%{release}
BuildRequires : buildreq-golang
Patch1: 0001-Add-Clear-Linux-Docker-integration-for-Kata-Containe.patch
Patch2: 0002-Set-kata-runtime-as-default-runtime-for-cri-o.patch
Patch3: 0003-Allow-extra-docker-opts-as-a-flag-to-dockerd.patch

%description
This directory and sub directories contain generated code.
The code is generated via go-swagger

%package bin
Summary: bin components for the kata-runtime package.
Group: Binaries
Requires: kata-runtime-data = %{version}-%{release}
Requires: kata-runtime-libexec = %{version}-%{release}
Requires: kata-runtime-license = %{version}-%{release}
Requires: kata-runtime-services = %{version}-%{release}

%description bin
bin components for the kata-runtime package.


%package data
Summary: data components for the kata-runtime package.
Group: Data

%description data
data components for the kata-runtime package.


%package libexec
Summary: libexec components for the kata-runtime package.
Group: Default
Requires: kata-runtime-license = %{version}-%{release}

%description libexec
libexec components for the kata-runtime package.


%package license
Summary: license components for the kata-runtime package.
Group: Default

%description license
license components for the kata-runtime package.


%package services
Summary: services components for the kata-runtime package.
Group: Systemd services

%description services
services components for the kata-runtime package.


%prep
%setup -q -n runtime-1.8.2
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
## build_prepend content
export GOPATH="${PWD}/gopath/"
mkdir -p "${GOPATH}/src/github.com/kata-containers/"
ln -sf "${PWD}" "${GOPATH}/src/github.com/kata-containers/runtime"
cd "${GOPATH}/src/github.com/kata-containers/runtime"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570488315
export GCC_IGNORE_WERROR=1
export GOPROXY=file:///usr/share/goproxy
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}  SKIP_GO_VERSION_CHECK=y QEMUCMD=kata-qemu-lite-system-x86_64


%install
export SOURCE_DATE_EPOCH=1570488315
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kata-runtime
cp LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/LICENSE
cp pkg/katatestutils/vendor/github.com/blang/semver/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/pkg_katatestutils_vendor_github.com_blang_semver_LICENSE
cp pkg/katatestutils/vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/pkg_katatestutils_vendor_github.com_davecgh_go-spew_LICENSE
cp pkg/katatestutils/vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/pkg_katatestutils_vendor_github.com_pmezard_go-difflib_LICENSE
cp pkg/katatestutils/vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/pkg_katatestutils_vendor_github.com_stretchr_testify_LICENSE
cp vendor/github.com/BurntSushi/toml/COPYING %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_BurntSushi_toml_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/toml-test-decoder/COPYING %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_BurntSushi_toml_cmd_toml-test-decoder_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/toml-test-encoder/COPYING %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_BurntSushi_toml_cmd_toml-test-encoder_COPYING
cp vendor/github.com/BurntSushi/toml/cmd/tomlv/COPYING %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_BurntSushi_toml_cmd_tomlv_COPYING
cp vendor/github.com/Microsoft/go-winio/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_Microsoft_go-winio_LICENSE
cp vendor/github.com/Microsoft/go-winio/archive/tar/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_Microsoft_go-winio_archive_tar_LICENSE
cp vendor/github.com/Microsoft/hcsshim/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_Microsoft_hcsshim_LICENSE
cp vendor/github.com/Microsoft/hcsshim/cmd/runhcs/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_Microsoft_hcsshim_cmd_runhcs_LICENSE
cp vendor/github.com/Microsoft/hcsshim/pkg/go-runhcs/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_Microsoft_hcsshim_pkg_go-runhcs_LICENSE
cp vendor/github.com/PuerkitoBio/purell/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_PuerkitoBio_purell_LICENSE
cp vendor/github.com/PuerkitoBio/urlesc/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_PuerkitoBio_urlesc_LICENSE
cp vendor/github.com/asaskevich/govalidator/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_asaskevich_govalidator_LICENSE
cp vendor/github.com/codahale/hdrhistogram/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_codahale_hdrhistogram_LICENSE
cp vendor/github.com/containerd/cgroups/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_cgroups_LICENSE
cp vendor/github.com/containerd/console/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_console_LICENSE
cp vendor/github.com/containerd/containerd/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_containerd_LICENSE
cp vendor/github.com/containerd/cri-containerd/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_cri-containerd_LICENSE
cp vendor/github.com/containerd/fifo/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_fifo_LICENSE
cp vendor/github.com/containerd/go-runc/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_go-runc_LICENSE
cp vendor/github.com/containerd/ttrpc/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_ttrpc_LICENSE
cp vendor/github.com/containerd/typeurl/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_typeurl_LICENSE
cp vendor/github.com/containernetworking/cni/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_containernetworking_cni_LICENSE
cp vendor/github.com/containernetworking/plugins/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_containernetworking_plugins_LICENSE
cp vendor/github.com/coreos/go-systemd/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_coreos_go-systemd_LICENSE
cp vendor/github.com/cri-o/cri-o/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_cri-o_cri-o_LICENSE
cp vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_davecgh_go-spew_LICENSE
cp vendor/github.com/dlespiau/covertool/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_dlespiau_covertool_LICENSE
cp vendor/github.com/docker/go-units/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_docker_go-units_LICENSE
cp vendor/github.com/globalsign/mgo/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_globalsign_mgo_LICENSE
cp vendor/github.com/globalsign/mgo/bson/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_globalsign_mgo_bson_LICENSE
cp vendor/github.com/globalsign/mgo/internal/json/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_globalsign_mgo_internal_json_LICENSE
cp vendor/github.com/go-ini/ini/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_go-ini_ini_LICENSE
cp vendor/github.com/go-openapi/analysis/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_analysis_LICENSE
cp vendor/github.com/go-openapi/errors/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_errors_LICENSE
cp vendor/github.com/go-openapi/jsonpointer/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_jsonpointer_LICENSE
cp vendor/github.com/go-openapi/jsonreference/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_jsonreference_LICENSE
cp vendor/github.com/go-openapi/loads/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_loads_LICENSE
cp vendor/github.com/go-openapi/runtime/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_runtime_LICENSE
cp vendor/github.com/go-openapi/runtime/middleware/denco/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_runtime_middleware_denco_LICENSE
cp vendor/github.com/go-openapi/spec/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_spec_LICENSE
cp vendor/github.com/go-openapi/spec/license.go %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_spec_license.go
cp vendor/github.com/go-openapi/strfmt/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_strfmt_LICENSE
cp vendor/github.com/go-openapi/swag/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_swag_LICENSE
cp vendor/github.com/go-openapi/validate/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_validate_LICENSE
cp vendor/github.com/godbus/dbus/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_godbus_dbus_LICENSE
cp vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_gogo_protobuf_LICENSE
cp vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_golang_protobuf_LICENSE
cp vendor/github.com/grpc-ecosystem/grpc-opentracing/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_grpc-ecosystem_grpc-opentracing_LICENSE
cp vendor/github.com/hashicorp/errwrap/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_hashicorp_errwrap_LICENSE
cp vendor/github.com/hashicorp/go-multierror/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_hashicorp_go-multierror_LICENSE
cp vendor/github.com/hashicorp/yamux/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_hashicorp_yamux_LICENSE
cp vendor/github.com/intel/govmm/COPYING %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_intel_govmm_COPYING
cp vendor/github.com/kata-containers/agent/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_kata-containers_agent_LICENSE
cp vendor/github.com/mailru/easyjson/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_mailru_easyjson_LICENSE
cp vendor/github.com/mdlayher/vsock/LICENSE.md %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_mdlayher_vsock_LICENSE.md
cp vendor/github.com/mitchellh/mapstructure/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_mitchellh_mapstructure_LICENSE
cp vendor/github.com/opencontainers/go-digest/LICENSE.code %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_opencontainers_go-digest_LICENSE.code
cp vendor/github.com/opencontainers/go-digest/LICENSE.docs %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_opencontainers_go-digest_LICENSE.docs
cp vendor/github.com/opencontainers/runc/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_opencontainers_runc_LICENSE
cp vendor/github.com/opencontainers/runtime-spec/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_opencontainers_runtime-spec_LICENSE
cp vendor/github.com/opentracing/opentracing-go/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_opentracing_opentracing-go_LICENSE
cp vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_pkg_errors_LICENSE
cp vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_pmezard_go-difflib_LICENSE
cp vendor/github.com/prometheus/procfs/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_prometheus_procfs_LICENSE
cp vendor/github.com/safchain/ethtool/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_safchain_ethtool_LICENSE
cp vendor/github.com/seccomp/libseccomp-golang/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_seccomp_libseccomp-golang_LICENSE
cp vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_sirupsen_logrus_LICENSE
cp vendor/github.com/stretchr/testify/LICENCE.txt %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_stretchr_testify_LICENCE.txt
cp vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_stretchr_testify_LICENSE
cp vendor/github.com/uber/jaeger-client-go/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_uber_jaeger-client-go_LICENSE
cp vendor/github.com/uber/jaeger-lib/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_uber_jaeger-lib_LICENSE
cp vendor/github.com/urfave/cli/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_urfave_cli_LICENSE
cp vendor/github.com/vishvananda/netlink/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_vishvananda_netlink_LICENSE
cp vendor/github.com/vishvananda/netns/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_github.com_vishvananda_netns_LICENSE
cp vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_golang.org_x_crypto_LICENSE
cp vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_golang.org_x_net_LICENSE
cp vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_golang.org_x_sys_LICENSE
cp vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_golang.org_x_text_LICENSE
cp vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_google.golang.org_genproto_LICENSE
cp vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_google.golang.org_grpc_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_gopkg.in_yaml.v2_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
cp vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/kata-runtime/vendor_gopkg.in_yaml.v2_NOTICE
cp virtcontainers/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/virtcontainers_LICENSE
cp virtcontainers/pkg/oci/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/virtcontainers_pkg_oci_LICENSE
%make_install SKIP_GO_VERSION_CHECK=y GOPATH="${PWD}/gopath/" PREFIX=/usr/
## install_append content
sed -i -e '/^initrd =/d' %{buildroot}/usr/share/defaults/kata-containers/configuration-qemu.toml
install -m 0755 -D set-docker-default-runtime %{buildroot}/usr/bin/set-docker-default-runtime
install -m 0644 -D clearlinux.conf %{buildroot}/usr/lib/systemd/system/docker.service.d/clearlinux.conf
install -m 0644 -D 50-runtime.conf %{buildroot}/usr/lib/systemd/system/docker.service.d/50-runtime.conf
install -m 0644 -D docker-set-runtime.service %{buildroot}/usr/lib/systemd/system/docker-set-runtime.service
install -m 0755 -D set-crio-default-runtime %{buildroot}/usr/bin/set-crio-default-runtime
install -m 0644 -D crio-clearlinux.conf %{buildroot}/usr/lib/systemd/system/crio.service.d/crio-clearlinux.conf
install -m 0644 -D crio-set-runtime.service %{buildroot}/usr/lib/systemd/system/crio-set-runtime.service
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/containerd-shim-kata-v2
/usr/bin/kata-collect-data.sh
/usr/bin/kata-runtime
/usr/bin/set-crio-default-runtime
/usr/bin/set-docker-default-runtime

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/kata-runtime
/usr/share/defaults/kata-containers/configuration-fc.toml
/usr/share/defaults/kata-containers/configuration-nemu.toml
/usr/share/defaults/kata-containers/configuration-qemu.toml
/usr/share/defaults/kata-containers/configuration.toml

%files libexec
%defattr(-,root,root,-)
/usr/libexec/kata-containers/kata-netmon

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kata-runtime/LICENSE
/usr/share/package-licenses/kata-runtime/pkg_katatestutils_vendor_github.com_blang_semver_LICENSE
/usr/share/package-licenses/kata-runtime/pkg_katatestutils_vendor_github.com_davecgh_go-spew_LICENSE
/usr/share/package-licenses/kata-runtime/pkg_katatestutils_vendor_github.com_pmezard_go-difflib_LICENSE
/usr/share/package-licenses/kata-runtime/pkg_katatestutils_vendor_github.com_stretchr_testify_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_BurntSushi_toml_COPYING
/usr/share/package-licenses/kata-runtime/vendor_github.com_BurntSushi_toml_cmd_toml-test-decoder_COPYING
/usr/share/package-licenses/kata-runtime/vendor_github.com_BurntSushi_toml_cmd_toml-test-encoder_COPYING
/usr/share/package-licenses/kata-runtime/vendor_github.com_BurntSushi_toml_cmd_tomlv_COPYING
/usr/share/package-licenses/kata-runtime/vendor_github.com_Microsoft_go-winio_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_Microsoft_go-winio_archive_tar_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_Microsoft_hcsshim_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_Microsoft_hcsshim_cmd_runhcs_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_Microsoft_hcsshim_pkg_go-runhcs_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_PuerkitoBio_purell_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_PuerkitoBio_urlesc_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_asaskevich_govalidator_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_codahale_hdrhistogram_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_cgroups_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_console_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_containerd_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_cri-containerd_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_fifo_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_go-runc_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_ttrpc_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_containerd_typeurl_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_containernetworking_cni_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_containernetworking_plugins_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_coreos_go-systemd_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_cri-o_cri-o_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_davecgh_go-spew_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_dlespiau_covertool_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_docker_go-units_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_globalsign_mgo_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_globalsign_mgo_bson_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_globalsign_mgo_internal_json_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_go-ini_ini_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_analysis_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_errors_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_jsonpointer_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_jsonreference_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_loads_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_runtime_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_runtime_middleware_denco_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_spec_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_spec_license.go
/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_strfmt_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_swag_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_go-openapi_validate_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_godbus_dbus_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_gogo_protobuf_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_golang_protobuf_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_grpc-ecosystem_grpc-opentracing_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_hashicorp_errwrap_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_hashicorp_go-multierror_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_hashicorp_yamux_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_intel_govmm_COPYING
/usr/share/package-licenses/kata-runtime/vendor_github.com_kata-containers_agent_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_mailru_easyjson_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_mdlayher_vsock_LICENSE.md
/usr/share/package-licenses/kata-runtime/vendor_github.com_mitchellh_mapstructure_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_opencontainers_go-digest_LICENSE.code
/usr/share/package-licenses/kata-runtime/vendor_github.com_opencontainers_go-digest_LICENSE.docs
/usr/share/package-licenses/kata-runtime/vendor_github.com_opencontainers_runc_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_opencontainers_runtime-spec_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_opentracing_opentracing-go_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_pkg_errors_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_pmezard_go-difflib_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_prometheus_procfs_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_safchain_ethtool_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_seccomp_libseccomp-golang_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_sirupsen_logrus_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_stretchr_testify_LICENCE.txt
/usr/share/package-licenses/kata-runtime/vendor_github.com_stretchr_testify_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_uber_jaeger-client-go_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_uber_jaeger-lib_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_urfave_cli_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_vishvananda_netlink_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_github.com_vishvananda_netns_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_golang.org_x_crypto_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_golang.org_x_net_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_golang.org_x_sys_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_golang.org_x_text_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_google.golang.org_genproto_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_google.golang.org_grpc_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_gopkg.in_yaml.v2_LICENSE
/usr/share/package-licenses/kata-runtime/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
/usr/share/package-licenses/kata-runtime/vendor_gopkg.in_yaml.v2_NOTICE
/usr/share/package-licenses/kata-runtime/virtcontainers_LICENSE
/usr/share/package-licenses/kata-runtime/virtcontainers_pkg_oci_LICENSE

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/crio-set-runtime.service
/usr/lib/systemd/system/crio.service.d/crio-clearlinux.conf
/usr/lib/systemd/system/docker-set-runtime.service
/usr/lib/systemd/system/docker.service.d/50-runtime.conf
/usr/lib/systemd/system/docker.service.d/clearlinux.conf
