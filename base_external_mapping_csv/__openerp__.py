# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2011 Zikzakmedia S.L. (http://zikzakmedia.com) All Rights Reserved.
#                       Raimon Esteve <resteve@zikzakmedia.com>
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Base External Mapping CSV",
    "author" : "Zikzakmedia SL",
    "website" : "http://www.zikzakmedia.com",
    "license" : "AGPL-3",
    "description" : """
OpenERP integration to External Mapping from CSV Files.
- Create OpenObject Model to External Model.
    """,
    "version" : "0.1",
    "depends" : [
        "base_external_mapping",
    ],
    "init_xml" : [],
    "update_xml" : [
        "base_external_mapping_csv_view.xml",
    ],
    "category" : "Generic Modules",
    "active": False,
    "installable": True
}
