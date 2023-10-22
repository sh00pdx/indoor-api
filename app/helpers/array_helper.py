class ArrayHelper:

    def remove_null_values(self, obj):
        if isinstance(obj, dict):
            return {
                key: self.remove_null_values(value)
                for key, value in obj.items()
                if value is not None
            }
        elif isinstance(obj, list):
            return [self.remove_null_values(item) for item in obj if item is not None]
        else:
            return obj
        
array_helper_singleton = ArrayHelper()