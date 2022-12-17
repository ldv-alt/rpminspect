/*
 * Copyright The rpminspect Project Authors
 * SPDX-License-Identifier: LGPL-3.0-or-later
 */

/*
 * Internal structures used for passing context information to callbacks
 */

#ifndef _LIBRPMINSPECT_CALLBACKS_H
#define _LIBRPMINSPECT_CALLBACKS_H

#include "types.h"

/* Context structure for add_ignores() and add_ignores_cb() in lib/init.c. */
typedef struct {
    string_list_map_t **inspection_ignores;
    const char *inspection;
} add_ignores_cb_data;

/* Context structure for tabledict() and tabledict_cb() in lib/init.c. */
typedef struct {
    bool required;
    bool single;
    string_map_t **table;
} tabledict_cb_data;

#endif /* _LIBRPMINSPECT_CALLBACKS_H */
