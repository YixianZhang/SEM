# Sampe API call for cellxgene_census
import cellxgene_census
import tiledbsoma

def query():
    with cellxgene_census.open_soma() as census:
        # Reads SOMADataFrame as a slice
        cell_metadata = census["census_data"]["homo_sapiens"].obs.read(
            value_filter="sex == 'female' and cell_type in ['microglial cell', 'neuron']",
            column_names=["assay", "cell_type", "tissue", "tissue_general", "suspension_type", "disease"]
        )

        # Concatenates results to pyarrow.Table
        cell_metadata = cell_metadata.concat()

        # Converts to pandas.DataFrame
        cell_metadata = cell_metadata.to_pandas()

        print(cell_metadata)

def obtain():
    with cellxgene_census.open_soma() as census:
        # Reads SOMADataFrame as a slice
        cell_metadata = census["census_data"]["homo_sapiens"].obs.read(
            value_filter="sex == 'female' and cell_type in ['microglial cell', 'neuron']",
            column_names=["assay", "cell_type", "tissue", "tissue_general", "suspension_type", "disease"]
        )

        # Concatenates results to pyarrow.Table
        cell_metadata = cell_metadata.concat()

        # Converts to pandas.DataFrame
        cell_metadata = cell_metadata.to_pandas()

        print(cell_metadata)

def memory_efficient_query():
    with cellxgene_census.open_soma() as census:
        human = census["census_data"]["homo_sapiens"]
        query = human.axis_query(
            measurement_name="RNA",
            obs_query=tiledbsoma.AxisQuery(
                value_filter="tissue == 'brain' and sex == 'male'"
            )
        )

        iterator = query.X("raw").tables()

        # Get an iterative slice as pyarrow.Table
        raw_slice = next(iterator)
        print(raw_slice)
        query.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # query()
    # obtain()
    memory_efficient_query()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
