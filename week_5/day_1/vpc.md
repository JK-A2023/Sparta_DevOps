# VPC - Virtual Private Cloud

- AWS is like a building that is shared between everyone that uses the public cloud.
- Everyone uses a default public, shared VPC.
- There is a default subnet for each availability zone.
- Custom VPC is like having your own flat in this building. Only you have access to it.
- Control on how people access your applications through the outside.
  - Create your own subnets.
- On Azure, there is no such thing as default VPC. VPC's are virtual network.

1. Internet Gateway - Doorway into VPC
   1. VPC 10.0.0.0/16 <- CIDR
   2. Uses router to direct traffic to the public subnet.
   3. Public Subnet
      1. App VM
      2. Security Group
   4. Invisible router directs database requests to database vm.
   5. Private Subnet
      1. Database VM
      2. Security Group