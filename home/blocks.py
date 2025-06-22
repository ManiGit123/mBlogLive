# StreamField live in here
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.db import models


class TitleandTexBlock(blocks.StructBlock):
    # "Title and Text and nothing in it"
    title = blocks.CharBlock(required=True, help_text="Add your Title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:
        template = "blocks/title_and_tex_block.html"
        icon = "edit"
        label = "Title & Text"


class CardBlock(blocks.StructBlock):
    # cards with image text and buttons by ListBlock
    title = blocks.CharBlock(required=True, help_text="Add your title")
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first",
                    ),
                ),
            ]
        )
    )

    class Meta:
        template = "blocks/cards_block.html"
        icon = "image"
        label = "Card Blocks"


class CarouselBlock(blocks.StructBlock):
    # cards with image text and buttons by ListBlock
    title = blocks.CharBlock(required=True, help_text="Add your title")
    message = blocks.CharBlock(required=True, help_text="Add your message")
    carousels = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
            ]
        )
    )

    class Meta:
        template = "blocks/carousel_block.html"
        icon = "image"
        label = "Carousel Blocks"


class AccordionBlock(blocks.StructBlock):
    # cards with image text and buttons by ListBlock
    title = blocks.CharBlock(required=True, help_text="Add your title")
    accordions = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.RichTextBlock(required=True, max_length=500)),
            ]
        )
    )

    class Meta:
        template = "blocks/accordion_block.html"
        icon = "list-ul"
        label = "Accordion Blocks"


class CTABlock(blocks.StructBlock):
    # simple call to action section
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(
        required=True,
        features=[
            "bold",
            "italic",
        ],
    )
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default="Learn More", max_length=40)

    class Meta:
        template = "blocks/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"


class RichTextBlock(blocks.RichTextBlock):
    # Rich text with all the features

    class Meta:
        template = "blocks/rich_text_block.html"
        icon = "doc-full"
        label = "Full Rich Text"


class SimpleRichTextBlock(blocks.RichTextBlock):
    # Rich text without (limited) all the features

    # way 2
    def __init__(
        self,
        required=True,
        help_text=None,
        editor="default",
        features=None,
        max_length=None,
        validators=(),
        search_index=True,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta:
        template = "blocks/rich_text_block.html"
        icon = "link"
        label = "Link - Simple Rich Text"


class DatePickerBlock(blocks.StructBlock):
    date_text = blocks.CharBlock(
        required=True, max_length=50, help_text="Add date text"
    )
    date_picker = blocks.DateBlock(required=True, help_text="Pick your date")

    class Meta:
        template = "blocks/date_picker_block.html"
        icon = "calendar"
        label = "Date Picker"


class ButtonLinkBlock(blocks.StructBlock):
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default="Learn More", max_length=40)

    class Meta:
        template = "blocks/button_picker_block.html"
        icon = "link-external"
        label = "Button Link"
