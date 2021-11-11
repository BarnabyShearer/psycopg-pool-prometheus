#!/usr/bin/env python3
"""Sphinx config."""

extensions = ["sphinxcontrib.autoprogram", "sphinx.ext.autodoc"]

project = "Exposes the pool stats maintained by psycopg3's connection pool to prometheus."
copyright = "2021, Barnaby Shearer"
author = "Barnaby Shearer"

master_doc = "index"