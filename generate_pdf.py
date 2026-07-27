#!/usr/bin/env python3
"""
Pure Python PDF generator for the System Design course book.
No external dependencies required - generates PDF from scratch using PDF spec.
"""

import re
import zlib
import datetime


class SimplePDF:
    """Minimal PDF generator using only Python standard library."""
    
    def __init__(self):
        self.pages = []
        self.current_page_content = []
        self.page_width = 612  # Letter size in points (8.5 x 11 inches)
        self.page_height = 792
        self.margin_left = 54
        self.margin_right = 54
        self.margin_top = 72
        self.margin_bottom = 72
        self.font_size = 10
        self.line_height = 14
        self.y_position = self.page_height - self.margin_top
        self.objects = []
        self.pages_refs = []
        
    def _escape_pdf_text(self, text):
        """Escape special PDF characters."""
        text = text.replace('\\', '\\\\')
        text = text.replace('(', '\\(')
        text = text.replace(')', '\\)')
        return text
    
    def new_page(self):
        """Start a new page."""
        if self.current_page_content:
            self.pages.append(self.current_page_content)
        self.current_page_content = []
        self.y_position = self.page_height - self.margin_top
    
    def _add_text_line(self, text, font_size=10, bold=False, x_offset=0):
        """Add a single line of text to current page."""
        if self.y_position < self.margin_bottom:
            self.new_page()
        
        font = "/F2" if bold else "/F1"
        x = self.margin_left + x_offset
        escaped = self._escape_pdf_text(text)
        self.current_page_content.append(
            f"BT {font} {font_size} Tf {x} {self.y_position:.1f} Td ({escaped}) Tj ET"
        )
        self.y_position -= font_size * 1.4
    
    def add_title(self, text):
        """Add a large title."""
        self.y_position -= 10
        self._add_text_line(text, font_size=20, bold=True)
        self.y_position -= 10
    
    def add_heading1(self, text):
        """Add H1 heading."""
        self.y_position -= 15
        if self.y_position < self.margin_bottom + 40:
            self.new_page()
        self._add_text_line(text, font_size=16, bold=True)
        self.y_position -= 5
    
    def add_heading2(self, text):
        """Add H2 heading."""
        self.y_position -= 10
        if self.y_position < self.margin_bottom + 30:
            self.new_page()
        self._add_text_line(text, font_size=13, bold=True)
        self.y_position -= 3
    
    def add_heading3(self, text):
        """Add H3 heading."""
        self.y_position -= 6
        if self.y_position < self.margin_bottom + 25:
            self.new_page()
        self._add_text_line(text, font_size=11, bold=True)
        self.y_position -= 2
    
    def add_paragraph(self, text):
        """Add a paragraph of text, wrapping lines."""
        if not text.strip():
            self.y_position -= 6
            return
        
        # Simple word wrapping
        max_chars = 85  # approximate characters per line at size 10
        words = text.split()
        line = ""
        for word in words:
            if len(line) + len(word) + 1 > max_chars:
                self._add_text_line(line, font_size=10)
                line = word
            else:
                line = (line + " " + word).strip()
        if line:
            self._add_text_line(line, font_size=10)
    
    def add_code_line(self, text):
        """Add a line of code (monospace appearance)."""
        if self.y_position < self.margin_bottom:
            self.new_page()
        self._add_text_line("  " + text, font_size=9, x_offset=10)
    
    def add_separator(self):
        """Add a horizontal separator."""
        self.y_position -= 15
    
    def add_blank_line(self):
        """Add blank space."""
        self.y_position -= self.line_height

    def process_markdown(self, md_text):
        """Process markdown text into PDF content."""
        lines = md_text.split('\n')
        in_code_block = False
        in_table = False
        
        for line in lines:
            # Code blocks
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                if in_code_block:
                    self.y_position -= 4
                else:
                    self.y_position -= 4
                continue
            
            if in_code_block:
                self.add_code_line(line)
                continue
            
            # Horizontal rules
            if line.strip() == '---' or line.strip() == '***':
                self.add_separator()
                continue
            
            # Headers
            if line.startswith('# ') and not line.startswith('# '):
                pass  # fall through
            
            if line.startswith('# '):
                self.add_title(line[2:].strip())
                continue
            elif line.startswith('## '):
                self.add_heading1(line[3:].strip())
                continue
            elif line.startswith('### '):
                self.add_heading2(line[4:].strip())
                continue
            elif line.startswith('#### '):
                self.add_heading3(line[5:].strip())
                continue
            
            # Tables - simple handling
            if '|' in line and line.strip().startswith('|'):
                # Clean up table formatting
                cells = [c.strip() for c in line.split('|') if c.strip()]
                if cells and not all(c.replace('-', '').replace(':', '') == '' for c in cells):
                    table_line = "  |  ".join(cells)
                    self._add_text_line(table_line, font_size=9)
                continue
            
            # Bold text - strip markdown markers for display
            display_line = line
            display_line = re.sub(r'\*\*(.+?)\*\*', r'\1', display_line)
            display_line = re.sub(r'__(.+?)__', r'\1', display_line)
            display_line = re.sub(r'\*(.+?)\*', r'\1', display_line)
            display_line = re.sub(r'`(.+?)`', r'\1', display_line)
            
            # List items
            if display_line.strip().startswith('- ') or display_line.strip().startswith('* '):
                bullet_text = "  * " + display_line.strip()[2:]
                self.add_paragraph(bullet_text)
                continue
            
            # Numbered lists
            numbered = re.match(r'^(\s*)\d+\.\s+(.+)', display_line)
            if numbered:
                self.add_paragraph("  " + display_line.strip())
                continue
            
            # Checkbox items
            if '- [ ]' in display_line or '- [x]' in display_line:
                display_line = display_line.replace('- [ ]', '  [ ]').replace('- [x]', '  [x]')
                self.add_paragraph(display_line)
                continue
            
            # Regular text
            if display_line.strip():
                self.add_paragraph(display_line)
            else:
                self.add_blank_line()
    
    def generate(self):
        """Generate the PDF bytes."""
        # Finalize last page
        if self.current_page_content:
            self.pages.append(self.current_page_content)
        
        # Build PDF structure
        pdf_objects = []
        
        # Object 1: Catalog
        pdf_objects.append("1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj")
        
        # Object 2: Pages (placeholder, will be updated)
        pages_kids = " ".join(f"{i+4} 0 R" for i in range(len(self.pages)))
        pdf_objects.append(
            f"2 0 obj\n<< /Type /Pages /Kids [{pages_kids}] /Count {len(self.pages)} >>\nendobj"
        )
        
        # Object 3: Font resources
        pdf_objects.append(
            "3 0 obj\n<< /Font << /F1 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> "
            "/F2 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >> >> >>\nendobj"
        )
        
        # Page objects (starting at object 4)
        obj_num = 4
        for page_content in self.pages:
            content_obj_num = obj_num + 1
            # Page object
            pdf_objects.append(
                f"{obj_num} 0 obj\n<< /Type /Page /Parent 2 0 R "
                f"/MediaBox [0 0 {self.page_width} {self.page_height}] "
                f"/Contents {content_obj_num} 0 R /Resources 3 0 R >>\nendobj"
            )
            # Content stream
            stream_content = "\n".join(page_content)
            stream_bytes = stream_content.encode('latin-1', errors='replace')
            pdf_objects.append(
                f"{content_obj_num} 0 obj\n<< /Length {len(stream_bytes)} >>\n"
                f"stream\n{stream_content}\nendstream\nendobj"
            )
            obj_num += 2
        
        # Build the PDF file
        output = "%PDF-1.4\n"
        offsets = []
        
        for obj_str in pdf_objects:
            offsets.append(len(output.encode('latin-1', errors='replace')))
            output += obj_str + "\n"
        
        # Cross-reference table
        xref_offset = len(output.encode('latin-1', errors='replace'))
        output += "xref\n"
        output += f"0 {len(pdf_objects) + 1}\n"
        output += "0000000000 65535 f \n"
        for offset in offsets:
            output += f"{offset:010d} 00000 n \n"
        
        # Trailer
        output += f"trailer\n<< /Size {len(pdf_objects) + 1} /Root 1 0 R >>\n"
        output += f"startxref\n{xref_offset}\n%%EOF\n"
        
        return output.encode('latin-1', errors='replace')


def main():
    print("Reading markdown file...")
    with open('/projects/sandbox/system-design-100-days.md', 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    print(f"Markdown file: {len(md_content)} characters")
    
    print("Generating PDF...")
    pdf = SimplePDF()
    pdf.process_markdown(md_content)
    
    pdf_bytes = pdf.generate()
    
    output_path = '/projects/sandbox/System_Design_in_100_Days.pdf'
    with open(output_path, 'wb') as f:
        f.write(pdf_bytes)
    
    print(f"PDF generated successfully!")
    print(f"Output: {output_path}")
    print(f"Size: {len(pdf_bytes) / 1024:.1f} KB")
    print(f"Pages: {len(pdf.pages)}")


if __name__ == '__main__':
    main()
