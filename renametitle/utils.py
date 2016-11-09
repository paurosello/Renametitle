def after_rename(self, method, old, new, merge):
    title_field = self.meta.autoname
    if title_field and "field:" in title_field:
        title_field_name = title_field.rpartition(':')[2]
        self.db_set(title_field_name, new, update_modified=False)
        self.save()
        self.notify_update()