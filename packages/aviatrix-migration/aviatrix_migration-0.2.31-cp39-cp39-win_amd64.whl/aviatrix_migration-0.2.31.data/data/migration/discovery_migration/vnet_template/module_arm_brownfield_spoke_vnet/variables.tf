variable "region" {}
variable "account_name" {}
variable "resource_group_name" {}
variable "vnet_name" {}
variable "vnet_cidr" {
  description = "CIDR used by the applications"
}
variable "avtx_cidr" {
  default     = ""
  description = "CIDR used by the Aviatrix gateways"
}
variable "avtx_gw_size" {}
variable "hpe" {
  default = true
}
variable "use_azs" {
  type = bool
}
variable "route_tables" {}
variable "switch_traffic" {
  type    = bool
  default = false
}
variable "disable_bgp_propagation" {
  type        = bool
  default     = true
  description = "Used to configure aviatrix_managed_main RTs"
}
variable "spoke_gw_name" {
  default = ""
}
variable "transit_gw" {
  default = ""
}
variable "tags" {
  description = "Map of tags to assign to the gateway."
  type        = map(any)
  default     = null
}

variable "domain" {
  description = "Provide security domain name to which spoke needs to be deployed. Transit gateway mus tbe attached and have segmentation enabled."
  type        = string
  default     = ""
}

variable "inspection" {
  description = "Set to true to enable east/west Firenet inspection. Only valid when transit_gw is East/West transit Firenet"
  type        = bool
  default     = false
}

output azurerm_route_table_aviatrix_managed {
  value = azurerm_route_table.aviatrix_managed
}

output azurerm_route_table_aviatrix_managed_main {
  value = azurerm_route_table.aviatrix_managed_main
}