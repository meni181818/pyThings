def unique_constraint_field_IntegrityError(field_name: str):
    try:
        Model.objects.create(whatever=whatever)
    except IntegrityError as e:
        table_name = Model.objects.model._meta.db_table
        column_name = Model._meta.get_field(field_name).column
        if f'UNIQUE constraint failed: {table_name}.{column_name}' in e.args:
        # or: if e.args == (f'UNIQUE constraint failed: {table_name}.{column_name}', ):
            print(f'got "UNIQUE constraint" error on: table: {table_name}, column: {column_name}')
