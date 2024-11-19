import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking App")
        self.root.geometry("800x600")

        # Set up default attributes
        self.image_path = None
        self.watermarked_image = None
        self.watermark_text = tk.StringVar()
        self.font_size = tk.IntVar(value=20)
        self.original_image = None

        # Load image button
        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        # Watermark text entry
        tk.Label(root, text="Watermark Text:").pack()
        self.text_entry = tk.Entry(root, textvariable=self.watermark_text)
        self.text_entry.pack()

        # Font size slider
        tk.Label(root, text="Font Size:").pack()
        self.size_slider = tk.Scale(root, from_=10, to=100, orient="horizontal", variable=self.font_size)
        self.size_slider.pack()

        # Add watermark button
        self.add_button = tk.Button(root, text="Add Watermark", command=self.add_watermark)
        self.add_button.pack()

        # Save image button
        self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.pack()

        # Image display area
        self.canvas = tk.Canvas(root, width=800, height=500, bg="gray")
        self.canvas.pack()

    def load_image(self):
        # Load an image file
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")])
        if not self.image_path:
            return
        self.original_image = Image.open(self.image_path)
        # Convert to RGBA to support transparency
        if self.original_image.mode != 'RGBA':
            self.original_image = self.original_image.convert('RGBA')
        self.display_image(self.original_image)

    def display_image(self, image):
        # Resize image maintaining aspect ratio
        display_size = (800, 500)
        image_aspect = image.width / image.height
        display_aspect = display_size[0] / display_size[1]

        if image_aspect > display_aspect:
            # Width is limiting factor
            new_width = display_size[0]
            new_height = int(new_width / image_aspect)
        else:
            # Height is limiting factor
            new_height = display_size[1]
            new_width = int(new_height * image_aspect)

        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.canvas_image = ImageTk.PhotoImage(resized_image)
        # Center the image on canvas
        x = (display_size[0] - new_width) // 2
        y = (display_size[1] - new_height) // 2
        self.canvas.create_image(x + new_width // 2, y + new_height // 2, image=self.canvas_image)

    def add_watermark(self):
        if not self.image_path:
            messagebox.showerror("Error", "No image loaded!")
            return

        watermark_text = self.watermark_text.get()
        if not watermark_text:
            messagebox.showerror("Error", "Please enter watermark text!")
            return

        font_size = self.font_size.get()

        # Create a copy of the original image
        self.watermarked_image = self.original_image.copy()
        draw = ImageDraw.Draw(self.watermarked_image)

        try:
            # Try to load Arial font
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            # Fallback to default font
            font = ImageFont.load_default()

        # Get text size using font.getbbox
        bbox = font.getbbox(watermark_text)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Calculate position (bottom-right corner with padding)
        padding = 20
        width, height = self.watermarked_image.size
        position = (width - text_width - padding, height - text_height - padding)

        # Create semi-transparent text
        # Draw text with slight shadow for better visibility
        shadow_position = (position[0] - 2, position[1] - 2)
        draw.text(shadow_position, watermark_text, font=font, fill=(0, 0, 0, 128))  # Shadow
        draw.text(position, watermark_text, font=font, fill=(255, 255, 255, 180))  # Main text

        self.display_image(self.watermarked_image)

    def save_image(self):
        if not self.watermarked_image:
            messagebox.showerror("Error", "No watermarked image to save!")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg *.jpeg")]
        )
        if save_path:
            # For JPEG files, convert to RGB before saving
            if save_path.lower().endswith(('.jpg', '.jpeg')):
                rgb_image = self.watermarked_image.convert('RGB')
                rgb_image.save(save_path, quality=95)
            else:
                self.watermarked_image.save(save_path)
            messagebox.showinfo("Success", f"Watermarked image saved to {save_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()