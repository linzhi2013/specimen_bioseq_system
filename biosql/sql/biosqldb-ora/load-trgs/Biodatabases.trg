--
-- SQL script to create the trigger(s) enabling the load API for
-- SGLD_Biodatabases.
--
-- Scaffold auto-generated by gen-api.pl.
--
--
-- $Id: Biodatabases.trg,v 1.1.1.2 2003-01-29 08:54:36 lapp Exp $
--

--
-- Copyright 2002-2003 Genomics Institute of the Novartis Research Foundation
-- Copyright 2002-2008 Hilmar Lapp
-- 
--  This file is part of BioSQL.
--
--  BioSQL is free software: you can redistribute it and/or modify it
--  under the terms of the GNU Lesser General Public License as
--  published by the Free Software Foundation, either version 3 of the
--  License, or (at your option) any later version.
--
--  BioSQL is distributed in the hope that it will be useful,
--  but WITHOUT ANY WARRANTY; without even the implied warranty of
--  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
--  GNU Lesser General Public License for more details.
--
--  You should have received a copy of the GNU Lesser General Public License
--  along with BioSQL. If not, see <http://www.gnu.org/licenses/>.
--

CREATE OR REPLACE TRIGGER BIUR_Biodatabases
       INSTEAD OF INSERT OR UPDATE
       ON SGLD_Biodatabases
       REFERENCING NEW AS new OLD AS old
       FOR EACH ROW
DECLARE
	pk		SG_BIODATABASE.OID%TYPE DEFAULT :new.DB_Oid;
	do_DML		INTEGER DEFAULT BSStd.DML_NO;
BEGIN
	IF INSERTING THEN
		do_DML := BSStd.DML_I;
	ELSE
		-- this is an update
		do_DML := BSStd.DML_UI;
	END IF;
	-- do insert or update (depending on whether it exists or not)
	pk := DB.get_oid(
			DB_OID => pk,
		        DB_NAME => DB_NAME,
			DB_ACRONYM => DB_ACRONYM,
			DB_ORGANIZATION => DB_ORGANIZATION,
			DB_URI => DB_URI,
			do_DML             => do_DML);
END;
/
