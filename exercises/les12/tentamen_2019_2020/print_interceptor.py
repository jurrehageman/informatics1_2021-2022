import sys
import io


class StdoutInterceptor:
    def connect(self):
        self.stdout_stored = sys.stdout
        self.stdout_buffer = io.StringIO()
        sys.stdout = self
        
    def write(self, output):
        print(output, file = self.stdout_stored, end = '')
        self.stdout_buffer.write(output)

    def flush(self):
        pass

    def getvalue(self):
        return self.stdout_buffer.getvalue()
    
    def stdout_contains_all(self, *words, ignore_case = False):
        print_output = self.stdout_buffer.getvalue()
        if ignore_case:
            print_output = print_output.upper()
            words = [word.upper() for word in words]
        for word in words:
            if print_output.find(word) <  0:
                return False
        return True

    def stdout_contains_any(self, *words, ignore_case = False):
        print_output = self.stdout_buffer.getvalue()
        if ignore_case:
            print_output = print_output.upper()
            words = [word.upper() for word in words]
        found_count = 0
        for word in words:
            if print_output.find(word) >= 0:
                found_count += 1
        return found_count > 0
    
    def detach(self):
        sys.stdout = self.stdout_stored

        
