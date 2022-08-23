import discord
import os
from discord.commands import option
from dotenv import load_dotenv
import mappings

bot = discord.Bot(debug_guilds=[1008162876877443152])
load_dotenv()
my_bot_token = os.environ.get('bot_token')

COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

LOTS_OF_COLORS = [
    "aliceblue",
    "antiquewhite",
    "aqua",
    "aquamarine",
    "azure",
    "beige",
    "bisque",
    "blueviolet",
    "brown",
    "burlywood",
    "cadetblue",
    "cornflowerblue",
    "cornsilk",
    "crimson",
    "cyan",
    "darkblue",
    "deepskyblue",
    "dimgray",
    "dimgrey",
    "dodgerblue",
    "firebrick",
    "floralwhite",
    "forestgreen",
    "fuchsia",
    "gainsboro",
    "ghostwhite",
    "gold",
    "goldenrod",
    "gray",
    "green",
    "greenyellow",
    "grey",
    "honeydew",
    "hotpink",
    "indianred",
    "indigo",
    "ivory",
    "khaki",
    "lavender",
    "lavenderblush",
    "lawngreen",
    "lightcoral",
    "maroon",
    "mediumaquamarine",
    "mediumblue",
    "mediumorchid",
    "midnightblue",
    "navajowhite",
    "navy",
    "oldlace",
    "olive",
    "olivedrab",
    "orange",
    "orangered",
    "orchid",
    "palegoldenrod",
    "palegreen",
    "plum",
    "powderblue",
    "purple",
    "red",
    "rosybrown",
    "royalblue",
    "saddlebrown",
    "sienna",
    "springgreen",
    "steelblue",
    "tan",
    "teal",
    "thistle",
    "tomato",
    "turquoise",
    "violet",
    "wheat",
    "white",
    "whitesmoke",
    "yellow",
    "yellowgreen",
]

# BASIC_ALLOWED = [217816539267727360]  # This would normally be a list of discord user IDs for the purpose of this example


async def color_searcher(ctx: discord.AutocompleteContext):
    """
    Returns a list of matching colors from the LOTS_OF_COLORS list.
    In this example, we've added logic to only display any results in the
    returned list if the user's ID exists in the BASIC_ALLOWED list.
    This is to demonstrate passing a callback in the discord.utils.basic_autocomplete function.
    """

    return [color for color in LOTS_OF_COLORS] # if ctx.interaction.user.id in BASIC_ALLOWED]


async def get_colors(ctx: discord.AutocompleteContext):
    """Returns a list of colors that begin with the characters entered so far."""
    return [color for color in COLORS if color.startswith(ctx.value.lower())]


async def get_animals(ctx: discord.AutocompleteContext):
    """Returns a list of animals that are (mostly) the color selected for the "color" option."""
    picked_color = ctx.options["color"]
    if picked_color == "red":
        return ["cardinal", "ladybug"]
    elif picked_color == "orange":
        return ["clownfish", "tiger"]
    elif picked_color == "yellow":
        return ["goldfinch", "banana slug"]
    elif picked_color == "green":
        return ["tree frog", "python"]
    elif picked_color == "blue":
        return ["blue jay", "blue whale"]
    elif picked_color == "indigo":
        return ["eastern indigo snake"]  # Needs to return an iterable even if only one item
    elif picked_color == "violet":
        return ["purple emperor butterfly", "orchid dottyback"]
    else:
        return ["rainbowfish"]


async def get_vacancy_labels(ctx: discord.AutocompleteContext):
    return list(mappings.vacancy_mapping.values())


@bot.slash_command(name="vacancies")
@option("label", description="Pick a role, a class, or a spec to see open vacancies.",
        autocomplete=discord.utils.basic_autocomplete(mappings.vacancy_mapping.values()))
async def vacancy_check(
    ctx: discord.ApplicationContext,
    label: str,
):
    color = mappings.get_color_from_label(label)
    if not color:
        await ctx.respond('Please match a vacancy category!', ephemeral=True)
    test_embed = discord.Embed(
        title=f'Showing {label} vacancies:',
        color=color
    )
    await ctx.respond(embed=test_embed, ephemeral=True)


@bot.slash_command(name="ac_example")
@option("color", description="Pick a color!", autocomplete=get_colors)
@option("animal", description="Pick an animal!", autocomplete=get_animals)
async def autocomplete_example(
    ctx: discord.ApplicationContext,
    color: str,
    animal: str,
):
    """
    Demonstrates using ctx.options to create options
    that are dependent on the values of other options.
    For the `color` option, a callback is passed, where additional
    logic can be added to determine which values are returned.
    For the `animal` option, the callback uses the input
    from the color option to return an iterable of animals
    """

    await ctx.respond(f"You picked {color} for the color, which allowed you to choose {animal} for the animal.")


@bot.slash_command(name="ac_basic_example")
@option(
    "color",
    description="Pick a color from this big list!",
    autocomplete=discord.utils.basic_autocomplete(color_searcher),
    # Demonstrates passing a callback to discord.utils.basic_autocomplete
)
@option(
    "animal",
    description="Pick an animal from this small list",
    autocomplete=discord.utils.basic_autocomplete(["snail", "python", "cricket", "orca"]),
    # Demonstrates passing a static iterable discord.utils.basic_autocomplete
)
async def autocomplete_basic_example(
    ctx: discord.ApplicationContext,
    color: str,
    animal: str,
):
    """
    This demonstrates using the discord.utils.basic_autocomplete helper function.
    For the `color` option, a callback is passed, where additional
    logic can be added to determine which values are returned.
    For the `animal` option, a static iterable is passed.
    While a small amount of values for `animal` are used in this example,
    iterables of any length can be passed to discord.utils.basic_autocomplete
    Note that the basic_autocomplete function itself will still only return a maximum of 25 items.
    """

    await ctx.respond(f"You picked {color} as your color, and {animal} as your animal!")


bot.run(my_bot_token)
