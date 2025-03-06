import msgspec
from architecture.utils.functions import run_sync
from intellibricks.llms.synapses import SynapseProtocol
from PIL import Image


def cast[T: msgspec.Struct](
    typ: T,
    img: Image,
    *,
    synapse: SynapseProtocol,
) -> T:
    return run_sync(
        cast_async,
        typ,
        img,
        synapse=synapse,
    )


async def cast_async[T: msgspec.Struct](
    typ: T,
    img: Image,
    *,
    synapse: SynapseProtocol,
) -> T: ...
