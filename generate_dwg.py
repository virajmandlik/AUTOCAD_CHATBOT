import os
import ezdxf

def create_dwg(rooms, filename):
    doc = ezdxf.new('R2010')
    msp = doc.modelspace()

    x_offset = 0
    for i, room in enumerate(rooms, start=1):
        width = room.get('width', 10)
        height = room.get('height', 10)
        
        # Create rectangle
        msp.add_lwpolyline([ 
            (x_offset, 0), 
            (x_offset + width, 0),
            (x_offset + width, height),
            (x_offset, height),
            (x_offset, 0)
        ])
        
        # Add room label
        msp.add_text(f"Room {i} ({width}x{height})", 
                    dxfattribs={
                        'height': 2,
                        'insert': (x_offset + width / 2, height / 2)
                    })
        x_offset += width + 5  # Add spacing between rooms

    file_path = os.path.join('static', filename)
    doc.saveas(file_path)
    return file_path
